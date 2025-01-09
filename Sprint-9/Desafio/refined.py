from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, monotonically_increasing_id, current_date, date_format, concat_ws, count, avg, year, row_number
from pyspark.sql.window import Window
from datetime import datetime

# Criar SparkSession
spark = SparkSession.builder \
    .appName("Refined Zone Processing") \
    .getOrCreate()

# Data de processamento
data_atual = datetime.now()
ano = data_atual.strftime("%Y")
mes = data_atual.strftime("%m")
dia = data_atual.strftime("%d")

# Diretório base para saída
bucket = "s3://vitor-data-lake/Refined/Parquet/"

# Caminhos de origem
trusted_csv_path = "s3://vitor-data-lake/Trusted/PARQUET/Movies/year=2025/month=01/day=03/"
trusted_tmdb_path = "s3://vitor-data-lake/Trusted/PARQUET/TMDB/year=2025/month=01/day=09/"

# Carregar os dados Trusted
df_csv = spark.read.parquet(trusted_csv_path).filter(col("genero").isin("Comedy", "Animation"))
df_tmdb = spark.read.parquet(trusted_tmdb_path).filter(col("genre_name").isin("Comedy", "Animation"))

# 1. Verificar e adicionar as colunas 'budget' e 'revenue' .
if 'budget' not in df_csv.columns:
    df_csv = df_csv.withColumn('budget', lit(None).cast('long'))
if 'revenue' not in df_csv.columns:
    df_csv = df_csv.withColumn('revenue', lit(None).cast('long'))

# 2. Criar DimArtista
dim_artista = df_csv.select(
    monotonically_increasing_id().alias("artista_id"),
    col("nomeArtista"),
    col("generoArtista"),
    col("profissao"),
    col("anoNascimento"),
    col("anoFalecimento"),
    col("titulosMaisConhecidos"),
    col("personagem")
).distinct()

dim_artista_path = f"{bucket}DimArtista/year={ano}/month={mes}/day={dia}/"
dim_artista.write.mode("overwrite").parquet(dim_artista_path)

# 3. Criar DimTempo
dim_tempo = df_tmdb.select(
    col("release_date").alias("data_completa")
).union(
    df_csv.select(col("anoLancamento").cast("string").alias("data_completa"))
).distinct()

dim_tempo = dim_tempo.withColumn("tempo_id", monotonically_increasing_id()) \
    .withColumn("ano", year(col("data_completa"))) \
    .withColumn("mes", date_format(col("data_completa"), "MM")) \
    .withColumn("dia", date_format(col("data_completa"), "dd"))

dim_tempo_path = f"{bucket}DimTempo/year={ano}/month={mes}/day={dia}/"
dim_tempo.write.mode("overwrite").parquet(dim_tempo_path)

# 4. Criar DimGenero
dim_genero = df_csv.select(
    col("genero").alias("nome_genero")
).union(
    df_tmdb.select(col("genre_name").alias("nome_genero"))
).distinct()

dim_genero = dim_genero.withColumn("genero_id", monotonically_increasing_id())

dim_genero_path = f"{bucket}DimGenero/year={ano}/month={mes}/day={dia}/"
dim_genero.write.mode("overwrite").parquet(dim_genero_path)

# 5. Criar DimObra
dim_obra_csv = df_csv.select(
    col("id").alias("obra_id"),
    col("tituloPincipal"),
    col("tituloOriginal"),
    col("genero").alias("nome_genero"),
    col("budget"),   # Garantir a coluna budget
    col("revenue")   # Garantir a coluna revenue
)

dim_obra_tmdb = df_tmdb.select(
    col("tmdb_id").alias("obra_id"),
    col("title").alias("tituloPincipal"),
    col("title").alias("tituloOriginal"),
    col("genre_name").alias("nome_genero"),
    col("budget"),   # Coluna budget já presente no TMDB
    col("revenue")   # Coluna revenue já presente no TMDB
)

dim_obra = dim_obra_csv.unionByName(dim_obra_tmdb, allowMissingColumns=True)

dim_obra = dim_obra.join(
    dim_genero, 
    dim_obra.nome_genero == dim_genero.nome_genero, 
    "left"
).select(
    dim_obra.obra_id,
    dim_obra.tituloPincipal,
    dim_obra.tituloOriginal,
    dim_genero.genero_id,
    dim_obra.nome_genero,
    dim_obra.budget,
    dim_obra.revenue
)

# Remover duplicados baseando-se no título principal e ID único
dim_obra_window = Window.partitionBy("tituloPincipal").orderBy(col("obra_id"))
dim_obra = dim_obra.withColumn("row_number", row_number().over(dim_obra_window))
dim_obra = dim_obra.filter(col("row_number") == 1).drop("row_number")

dim_obra_path = f"{bucket}DimObra/year={ano}/month={mes}/day={dia}/"
dim_obra.write.mode("overwrite").parquet(dim_obra_path)

# 6. Criar FatoObras
fato_obras_csv = df_csv.select(
    col("id").alias("obra_id"),
    col("anoLancamento").alias("data_completa"),
    col("tempoMinutos"),
    lit(None).cast("double").alias("vote_average"),
    col("budget"),   # Agora com a coluna budget
    col("revenue"),  # Agora com a coluna revenue
    col("nomeArtista"),
    col("genero").alias("nome_genero")
)

fato_obras_tmdb = df_tmdb.select(
    col("tmdb_id").alias("obra_id"),
    col("release_date").alias("data_completa"),
    lit(None).cast("double").alias("tempoMinutos"),
    col("vote_average"),
    col("budget"),   # Coluna budget já presente no TMDB
    col("revenue"),  # Coluna revenue já presente no TMDB
    lit(None).cast("string").alias("nomeArtista"),
    col("genre_name").alias("nome_genero")
)

fato_obras = fato_obras_csv.unionByName(fato_obras_tmdb)

fato_obras = fato_obras.join(
    dim_tempo,
    fato_obras.data_completa == dim_tempo.data_completa,
    "left"
).join(
    dim_genero,
    fato_obras.nome_genero == dim_genero.nome_genero,
    "left"
).join(
    dim_artista,
    fato_obras.nomeArtista == dim_artista.nomeArtista,
    "left"
)

# Selecionar colunas finais e baseando-se nas métricas principais
fato_obras = fato_obras.select(
    col("obra_id"),
    col("tempo_id"),
    col("genero_id"),
    col("artista_id"),
    col("tempoMinutos"),
    col("vote_average"),
    col("budget"),    # Manter orçamento
    col("revenue")    # Manter receita
).distinct()

fato_obras_path = f"{bucket}FatoObras/year={ano}/month={mes}/day={dia}/"
fato_obras.write.mode("overwrite").parquet(fato_obras_path)

# Finalizar SparkSession
spark.stop()
