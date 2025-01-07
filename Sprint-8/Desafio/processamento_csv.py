import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from awsglue.utils import getResolvedOptions

# Coleta dos argumentos para caminhos
args = getResolvedOptions(sys.argv, ['RAW_PATH', 'TRUSTED_PATH'])
RAW_PATH = args['RAW_PATH']
TRUSTED_PATH = args['TRUSTED_PATH']

# Criação da sessão Spark
sc = SparkContext()
spark = SparkSession(sc)

# Leitura do CSV com delimitador "|"
df = spark.read.csv(RAW_PATH, header=True, sep="|", inferSchema=True)

# Determina quais colunas estão completamente nulas ou inválidas
def get_valid_columns(df):
    valid_columns = []
    for column in df.columns:
        # Checa se há pelo menos uma linha válida na coluna (não nula ou não vazia)
        if df.filter(col(column).isNotNull() & (col(column) != "")).count() > 0:
            valid_columns.append(column)
    return valid_columns

# Identificar colunas válidas
valid_columns = get_valid_columns(df)

# Selecionar apenas colunas válidas
df = df.select(*valid_columns)

# Remoção de duplicados com base no ID
if "id" in df.columns:
    df = df.dropDuplicates(["id"])

if "genero" in df.columns:
    # Validar o gênero (excluir registros com gênero nulo ou inválido)
    df = df.filter(col("genero").isNotNull() & (col("genero") != ""))

# Adiciona as colunas de particionamento: ano, mês e dia (data atual)
current_date_str = datetime.now().strftime("%Y-%m-%d")
year_val = current_date_str.split("-")[0]
month_val = current_date_str.split("-")[1]
day_val = current_date_str.split("-")[2]

# Adiciona as colunas de particionamento
df_with_partitions = movie_genre_combined_df.withColumn("year", col("release_date").substr(1, 4)) \
                                           .withColumn("month", col("release_date").substr(6, 2)) \
                                           .withColumn("day", col("release_date").substr(9, 2))

# Modificação para o caminho correto, conforme data atual
current_path = f"{TRUSTED_PATH}/year={year_val}/month={month_val}/day={day_val}/"

# Escrever o dataframe como Parquet
df_with_partitions.write.mode("overwrite").parquet(current_path)

