import json
import boto3
import csv
import os
from datetime import datetime
from io import StringIO
from tmdbv3api import TMDb, Discover

# Configuração do TMDb
tmdb = TMDb()
tmdb.api_key = os.getenv('TMDB_API_KEY')  # A chave será lida da variável de ambiente
tmdb.language = 'pt-BR'

tmdb_discover = Discover()

bucket_name = 'vitor-data-lake'
movies_path = 'Raw/Local/CSV/Movies/2024/11/27/movies.csv'

# Configuração do S3
s3_client = boto3.client('s3')

class S3Handler:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def read_csv_from_s3_in_chunks(self, file_path: str, chunk_size: int = 100):
        
        response = s3_client.get_object(Bucket=self.bucket_name, Key=file_path)
        content = response['Body'].read().decode('utf-8')
        csv_data = StringIO(content)
        csv_reader = csv.DictReader(csv_data, delimiter='|')
        batch = []
        for row in csv_reader:
            if len(batch) >= chunk_size:
                yield batch  # Retorna a parte de dados acumulada
                batch = []  # Resetando o lote para o próximo
            batch.append(row)
        if batch:
            yield batch  # Garantir que o último lote seja retornado
    

    def save_json_to_s3(self, data: list, nome_arquivo: str):
        
        data_atual = datetime.now().strftime('%Y/%m/%d')
        caminho = f"Raw/TMDB/JSON/{data_atual}/{nome_arquivo}.json"
        s3_client.put_object(Bucket=self.bucket_name, Key=caminho, Body=json.dumps(data, ensure_ascii=False))
        print(f"Dados salvos em s3://{self.bucket_name}/{caminho}")
    

    def buscar_por_genero(self, genero_id, tipo='movie', max_paginas=3):
        resultados = []
        for pagina in range(1, max_paginas + 1):
            
            if tipo == 'movie':
                items = tmdb_discover.discover_movies({'page': pagina, 'with_genres': genero_id})
            else:
                items = tmdb_discover.discover_tv_shows({'page': pagina, 'with_genres': genero_id})

            if not items:
                break

            for item in items:
                resultados.append({
                    'tmdb_id': item.id,
                    'title': item.title if tipo == 'movie' else item.name,
                    'overview': item.overview,
                    'release_date': item.release_date if tipo == 'movie' else item.first_air_date,
                    'vote_average': item.vote_average
                })
        return resultados

def processar_dados_em_pedacos(s3_handler: S3Handler):
    # Lendo o arquivo em pedaços para evitar o estouro de memória
    dados_processados = []
    chunk_size = 100
    for i, batch in enumerate(s3_handler.read_csv_from_s3_in_chunks(movies_path, chunk_size)):
        print(f"Processando lote {i + 1} com {len(batch)} registros")

        # Processa dados do lote
        for row in batch:
            dados_processados.append(row)  # Processamento do CSV (enriquecimento pode ser adicionado aqui)

        # Salve após processar cada bloco para reduzir o uso de memória
        if dados_processados:
            s3_handler.save_json_to_s3(dados_processados, f'movies_processed_part_{i+1}')
            dados_processados.clear()  # Limpar a lista após salvar para economizar memória

    print("Processamento do arquivo CSV concluído.")

    # Busca por gêneros
    print("Iniciando busca por gêneros.")
    generos = [35, 16]  # IDs para Comédia e Animação
    for genero in generos:
        tipo = 'movie'
        resultados_genero = s3_handler.buscar_por_genero(genero, tipo=tipo)
        if resultados_genero:
            s3_handler.save_json_to_s3(resultados_genero, f'{tipo}_genre_{genero}')

    print("Processamento concluído para todos os gêneros.")

def lambda_handler(event, context):
    s3_handler = S3Handler(bucket_name)

    processar_dados_em_pedacos(s3_handler)

    return {"status": "Processamento finalizado"}
