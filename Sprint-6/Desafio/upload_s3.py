import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def upload_s3(nome_bucket, arquivo_local_path, raw_zone_path):
    s3 = boto3.client('s3', region_name='us-east-1')
    
    data_atual = datetime.now().strftime('%Y/%m/%d')
    nome_arquivo = os.path.basename(arquivo_local_path)
    
    s3_caminho = f"{raw_zone_path}/{data_atual}/{nome_arquivo}"
    s3.upload_file(arquivo_local_path, nome_bucket, s3_caminho)
    print(f"Arquivo {nome_arquivo} enviado para {nome_bucket}/{s3_caminho}")
    
# Config
nome_bucket = "vitor-data-lake"
raw_zone_path_movies = "Raw/Local/CSV/Movies"
raw_zone_path_series = "Raw/Local/CSV/Series"

# Caminhos locais dos arquivos no Dockerfile
local_arquivo_movies = "/app/Filmes+e+Series/movies.csv"
local_arquivo_series = "/app/Filmes+e+Series/series.csv"

# Envio dos arquivos para o S3
upload_s3(nome_bucket, local_arquivo_movies, raw_zone_path_movies)
upload_s3(nome_bucket, local_arquivo_series, raw_zone_path_series)

