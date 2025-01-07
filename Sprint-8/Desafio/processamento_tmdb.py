import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_date, year, month, dayofmonth
from awsglue.utils import getResolvedOptions
from datetime import datetime

# Coleta dos argumentos para caminhos
args = getResolvedOptions(sys.argv, ['RAW_PATH', 'TRUSTED_PATH'])
RAW_PATH = args['RAW_PATH']
TRUSTED_PATH = args['TRUSTED_PATH']

# Criação da sessão Spark
sc = SparkContext()
spark = SparkSession(sc)

# Caminhos dos arquivos JSON no S3
movie_genre_35_path = RAW_PATH + "movie_genre_35.json"
movie_genre_16_path = RAW_PATH + "movie_genre_16.json"

# Leitura dos arquivos JSON
movie_genre_35_df = spark.read.json(movie_genre_35_path)
movie_genre_16_df = spark.read.json(movie_genre_16_path)

# Combina os dois dataframes (Comédia e Animação)
movie_genre_combined_df = movie_genre_35_df.union(movie_genre_16_df)

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
