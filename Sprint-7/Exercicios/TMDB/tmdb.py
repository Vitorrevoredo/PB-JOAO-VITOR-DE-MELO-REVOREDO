import requests
import pandas as pd
from IPython.display import display
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv(r"C:\Users\Vitor\Documents\GitHub\PB-JOAO-VITOR-DE-MELO-REVOREDO\Sprint-7\Exercicios\TMDB\.env")
api_key = os.getenv("TMDB_API_KEY")

# URL para requisição
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

# Fazer a requisição à API
response = requests.get(url)
data = response.json() 

filmes = []


for movie in data['results']:
    df = {
        'Titulo': movie['title'],  
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df)


df_filmes = pd.DataFrame(filmes)
display(df_filmes)
