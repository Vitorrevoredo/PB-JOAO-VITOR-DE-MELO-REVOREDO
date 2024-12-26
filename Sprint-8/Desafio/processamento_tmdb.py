import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, lit
from awsglue.utils import getResolvedOptions
from datetime import datetime

# Função para validar colunas
def get_valid_columns(df):
    """
    Retorna apenas colunas que possuem ao menos um valor válido (não nulo).
    """
    valid_columns = [column for column in df.columns if df.filter(col(column).isNotNull()).limit(1).count() > 0]
    return df.select(*valid_columns)

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

# Remove colunas completamente inválidas
df = get_valid_columns(df)

# Limpeza básica dos dados (somente se as colunas forem válidas)
if "tmdb_id" in df.columns:
    df = df.filter(col("tmdb_id").isNotNull())

if "release_date" in df.columns:
    df = df.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd"))
    df = df.filter(col("release_date").isNotNull())

# Aplicando filtros em colunas condicionais
if "vote_average" in df.columns:
    df = df.filter(
        (col("vote_average").isNotNull() & (col("vote_average") > 0)) | col("vote_average").isNull()
    )

# Adicionando colunas para particionamento e data de processamento
current_date = datetime.now()
df = (
    df
    .withColumn("processing_date", lit(current_date))
    .withColumn("year", lit(current_date.year))
    .withColumn("month", lit(current_date.month))
    .withColumn("day", lit(current_date.day))
)

# Persistindo os dados na Trusted Zone com particionamento
print(f"Gravando os dados limpos em: {TRUSTED_PATH}")
df.write.partitionBy("year", "month", "day").mode("overwrite").parquet(TRUSTED_PATH)