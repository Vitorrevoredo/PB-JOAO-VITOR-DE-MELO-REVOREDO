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

# Persistir em formato Parquet na camada Trusted
df.write.mode("overwrite").parquet(TRUSTED_PATH)
