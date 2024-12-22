import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, lit
from awsglue.utils import getResolvedOptions
from datetime import datetime

# Coleta dos argumentos para caminhos
args = getResolvedOptions(sys.argv, ['RAW_PATH', 'TRUSTED_PATH'])
RAW_PATH = args['RAW_PATH']
TRUSTED_PATH = args['TRUSTED_PATH']

# Criação da sessão Spark
sc = SparkContext()
spark = SparkSession(sc)

# Leitura do JSON da camada Raw
print(f"Lendo os dados de: {RAW_PATH}")
df = spark.read.json(RAW_PATH)

# Total de registros antes da limpeza
print(f"Total de registros antes da limpeza: {df.count()}")

# Limpeza básica dos dados
df_cleaned = df.filter(
    (col("tmdb_id").isNotNull()) &  # Mantém apenas registros com tmdb_id
    (col("release_date").isNotNull())  # Mantém registros com data de lançamento
).withColumn(
    "release_date", to_date(col("release_date"), "yyyy-MM-dd")  # Converte para formato de data
).filter(col("release_date").isNotNull())  # Filtra datas inválidas

# Quantidade de registros após a limpeza inicial
print(f"Total de registros após a limpeza inicial: {df_cleaned.count()}")

# Aplicando filtros adicionais para valores de `vote_average`
df_cleaned = df_cleaned.filter(
    (col("vote_average").isNotNull() & (col("vote_average") > 0)) | col("vote_average").isNull()
)

# Adicionando colunas para particionamento e data de processamento
current_date = datetime.now()
df_cleaned = (
    df_cleaned
    .withColumn("processing_date", lit(current_date))
    .withColumn("year", lit(current_date.year))
    .withColumn("month", lit(current_date.month))
    .withColumn("day", lit(current_date.day))
)

# Verifique novamente o total após a limpeza final
print(f"Total de registros após a limpeza final: {df_cleaned.count()}")

# Persistindo os dados na Trusted Zone com particionamento
print(f"Gravando os dados limpos em: {TRUSTED_PATH}")
df_cleaned.write.partitionBy("year", "month", "day").mode("overwrite").parquet(TRUSTED_PATH)

print("Dados salvos com sucesso na camada Trusted.")
