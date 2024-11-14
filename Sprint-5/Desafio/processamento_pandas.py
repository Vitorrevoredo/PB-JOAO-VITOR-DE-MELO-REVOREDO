import pandas as pd
import boto3
from io import StringIO

# Configurações
bucket_name = 'bucket-desafio-vitor'
file_name = 'VendasTesouroDireto.csv'
output_file = 'C:/Users/Vitor/Documents/trabalho/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-5/Desafio/VendasTesouroDireto_modificado.csv'

# Conectando ao S3 e lendo o arquivo
s3 = boto3.client('s3')
csv_data = s3.get_object(Bucket=bucket_name, Key=file_name)['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_data), sep=';')

# Converter as colunas 'PU' e 'Valor' para numérico
df['PU'] = pd.to_numeric(df['PU'], errors='coerce')
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors = 'coerce')
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

# 4.1 Filtrando dados onde PU > 1000 e Quantidade < 50
df_filtrado = df[(df['PU'] > 1000) & (df['Quantidade'] < 50)]
print("\nFiltrando dados onde PU > 1000 e Quantidade < 50:\n", df_filtrado)

# 4.2 Funções de Agregação (Soma e Média)
media_pu = df['PU'].mean()
soma_valor = df['Valor'].sum()
print(f"\nMédia do PU: {media_pu}")
print(f"Soma do Valor: {soma_valor}")

# 4.3 Função Condicional para Categorizar 'Valor'
df['Categoria Valor'] = df['Valor'].apply(lambda x: 'Alto' if x > 100000 else 'Baixo')

# 4.4 Conversão de 'Data Venda' e extração de 'Ano Venda'
df['Data Venda'] = pd.to_datetime(df['Data Venda'], format='%d/%m/%Y', errors='coerce')
df['Ano Venda'] = df['Data Venda'].dt.year

# 4.6 Conversão de 'Tipo Titulo' para maiúsculas
df['Tipo Titulo'] = df['Tipo Titulo'].str.upper()

# Salvar o DataFrame modificado em um novo CSV
df.to_csv(output_file, index=False, sep=';')

# Carregar o arquivo modificado para o S3
s3.upload_file(output_file, bucket_name, 'VendasTesouroDireto_modificado.csv')
print(f'Arquivo modificado carregado com sucesso para o bucket {bucket_name}.')
