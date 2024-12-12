import os
import json
import boto3
import tmdbv3api
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Configuração da API TMDB
tmdb = tmdbv3api.TMDb()
tmdb.api_key = os.getenv('TMDB_API_KEY')
tmdb.language = 'pt-BR'

# Configuração do S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name='us-east-1'
)
bucket_name = 'vitor-data-lake'

# Caminhos dos arquivos no S3
movies_csv_path = 'Raw/Local/CSV/Movies/2024/11/27/movies.csv'
series_csv_path = 'Raw/Local/CSV/Series/2024/11/27/series.csv'

def inspecionar_dados(df, nome): # Para inspecionar DataFrame
    if df is not None:
        print(f"\nPrimeiros registros de {nome}:")
        print(df.head())
        print(f"\nInformações sobre {nome}:")
        print(df.info())

def ler_arquivo_s3(file_path): #  Lê arquivo do S3 e retorna como DataFrame
    print(f"Lendo arquivo {file_path} do S3...")
    response = s3_client.get_object(Bucket=bucket_name, Key=file_path)
    df = pd.read_csv(response['Body'], delimiter='|', low_memory=False)
    print(f"Colunas disponíveis em {file_path}:", df.columns.tolist())
    return df

def buscar_detalhes_tmdb(imdb_id): # Busca detalhes do filme/série no TMDB usando IMDb ID
    search = tmdbv3api.Search()
    movie = tmdbv3api.Movie()
    
    # Busca o ID do TMDB usando o IMDb ID
    results = search.movies(query=imdb_id, external_source="imdb_id")
    
    if results:
        tmdb_id = results[0].id
        # Busca detalhes completos
        details = movie.details(tmdb_id)
        
        # Buscar elenco
        credits = movie.credits(tmdb_id)
        
        # Buscar recomendações
        recommendations = movie.recommendations(tmdb_id)
        
        return {
            'tmdb_id': tmdb_id,
            'title': details.title,
            'overview': details.overview,
            'release_date': details.release_date,
            'genres': [genre.name for genre in details.genres],  # extrair os gêneros
            'vote_average': details.vote_average,
            'similar_movies': [m.id for m in movie.similar(tmdb_id)],
            'cast': [cast_member.name for cast_member in credits.cast],  # Elenco
            'recommendations': [rec.id for rec in recommendations.results]  # Recomendações
        }

def buscar_por_genero(genero_id, tipo='movie', max_paginas=3): # Busca filmes/séries por gênero
    discover = tmdbv3api.Discover()
    resultados = []
    
    for pagina in range(1, max_paginas + 1):
        if tipo == 'movie':
            items = discover.discover_movies({
                'page': pagina,
                'with_genres': genero_id
            })
        else:
            items = discover.discover_tv_shows({
                'page': pagina,
                'with_genres': genero_id
            })
        
        if not items:
            break
            
        resultados.extend(items)
    return resultados
    
def salvar_no_s3(dados, nome_arquivo): # Salva dados no S3 em formato JSON  
    data_atual = datetime.now().strftime('%Y/%m/%d')
    caminho = f"Raw/TMDB/JSON/{data_atual}/{nome_arquivo}.json"
    
    # Dividir dados em blocos de 100 registros, se necessário
    chunk_size = 100
    for i in range(0, len(dados), chunk_size):
        chunk = dados[i:i+chunk_size]
        # Verificar o tamanho do arquivo antes de salvar
        chunk_json = json.dumps(chunk, ensure_ascii=False)
        if len(chunk_json.encode('utf-8')) <= 10 * 1024 * 1024:  # 10MB
            s3_client.put_object(
                Bucket=bucket_name,
                Key=caminho,
                Body=chunk_json
            )
            print(f"Dados salvos em s3://{bucket_name}/{caminho}")
        else:
            print(f"Erro: O tamanho dos dados excede 10MB.")

def processar_dados(): # Função principal de processamento
    # Lê os arquivos do S3
    movies_df = ler_arquivo_s3(movies_csv_path)
    series_df = ler_arquivo_s3(series_csv_path)
    
    dados_processados = []
    
    # Processa filmes
    if movies_df is not None:
        if 'imdb_id' not in movies_df.columns:
            print("Aviso: Coluna 'imdb_id' não encontrada no DataFrame de filmes")
            print("Colunas disponíveis:", movies_df.columns.tolist())
        else:
            for _, row in movies_df.iterrows():
                imdb_id = row.get('imdb_id')  # Tentar pegar 'imdb_id', se não, usar 'id'
                if not imdb_id:
                    imdb_id = row.get('id')  # Caso 'imdb_id' não exista, usar 'id'
                if imdb_id:
                    detalhes = buscar_detalhes_tmdb(imdb_id)
                    if detalhes:
                        dados_processados.append(detalhes)
    
    # Processa séries
    if series_df is not None:
        if 'imdb_id' not in series_df.columns:
            print("Aviso: Coluna 'imdb_id' não encontrada no DataFrame de séries")
            print("Colunas disponíveis:", series_df.columns.tolist())
        else:
            for _, row in series_df.iterrows():
                imdb_id = row.get('imdb_id')  # Tentar pegar 'imdb_id', se não, usar 'id'
                if not imdb_id:
                    imdb_id = row.get('id')  # Caso 'imdb_id' não exista, usar 'id'
                if imdb_id:
                    detalhes = buscar_detalhes_tmdb(imdb_id)
                    if detalhes:
                        dados_processados.append(detalhes)
    
    # Busca filmes adicionais por gênero
    generos = [35, 16]  # Comédia e Animação
    for genero in generos:
        filmes_genero = buscar_por_genero(genero)
        for filme in filmes_genero:
            dados_processados.append({
                'tmdb_id': filme.id,
                'title': filme.title,
                'overview': filme.overview,
                'release_date': filme.release_date,
                'genres': [g['name'] for g in filme.genres] if hasattr(filme, 'genres') else [],  # Correção aqui
                'vote_average': filme.vote_average
            })
    
    # Salva os resultados
    if dados_processados:
        salvar_no_s3(dados_processados, 'dados_enriquecidos_tmdb')
    else:
        print("Nenhum dado foi processado.")

if __name__ == '__main__': # Inspeção inicial dos dados
    movies_df = ler_arquivo_s3(movies_csv_path)
    series_df = ler_arquivo_s3(series_csv_path)
    
    inspecionar_dados(movies_df, "filmes")
    inspecionar_dados(series_df, "séries")
    
    # Processamento principal
    processar_dados()
