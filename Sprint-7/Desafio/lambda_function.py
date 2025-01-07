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

    def save_json_to_s3(self, data: list, nome_arquivo: str):
        try:
            data_atual = datetime.now().strftime('%Y/%m/%d')
            caminho = f"Raw/TMDB/JSON/{data_atual}/{nome_arquivo}.json"
            s3_client.put_object(Bucket=self.bucket_name, Key=caminho, Body=json.dumps(data, ensure_ascii=False))
            print(f"Dados salvos em s3://{self.bucket_name}/{caminho}")
        except Exception as e:
            print(f"Erro ao salvar no S3: {str(e)}")

    def buscar_por_genero(self, genero_id, tipo='movie', max_paginas=3):
        resultados = []
        for pagina in range(1, max_paginas + 1):
            try:
                if tipo == 'movie':
                    items = tmdb_discover.discover_movies({'page': pagina, 'with_genres': genero_id})
                else:
                    items = tmdb_discover.discover_tv_shows({'page': pagina, 'with_genres': genero_id})

                if not items:
                    break

                for item in items:
                    # Identificar o nome do gênero diretamente
                    genero_nome = None
                    for genre in item.genre_ids:
                        if genre == genero_id:
                            # O nome do gênero será identificado com base no id que estamos passando
                            if genero_id == 35:  # Comédia
                                genero_nome = 'Comedy'
                            elif genero_id == 16:  # Animação
                                genero_nome = 'Animation'
                            break

                    resultados.append({
                        'tmdb_id': item.id,
                        'title': item.title if tipo == 'movie' else item.name,
                        'overview': item.overview,
                        'release_date': item.release_date if tipo == 'movie' else item.first_air_date,
                        'vote_average': item.vote_average,
                        'genre_name': genero_nome  # Nome do gênero no resultado
                    })
            except Exception as e:
                print(f"Erro na busca por gênero {genero_id} na página {pagina}: {str(e)}")
        return resultados

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
