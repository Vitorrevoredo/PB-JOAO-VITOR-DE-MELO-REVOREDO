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

# Limpeza básica dos dados
# 1. Remover linhas com valores nulos ou campos críticos faltando
df = df.na.drop(subset=["id", "tituloPincipal", "anoLancamento"])

# 2. Garantir que o ano de lançamento seja numérico e maior que 1888 (primeiro ano de filmes conhecidos)
df = df.filter((col("anoLancamento").cast("int").isNotNull()) & (col("anoLancamento") > 1888))

# 3. Validar o gênero (excluir registros com gênero nulo ou inválido)
df = df.filter(col("genero").isNotNull())

# 4. Opcional: Filtrar filmes com número suficiente de votos e boa nota média (exemplo: mais de 100 votos e nota média > 5)
df = df.filter((col("numeroVotos") > 100) & (col("notaMedia") > 5))

# Persistir em formato Parquet na camada Trusted
df.write.mode("overwrite").parquet(TRUSTED_PATH)
