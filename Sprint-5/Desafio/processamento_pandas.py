import pandas as pd
import boto3
from io import StringIO

# Nome do bucket e arquivo no S3
bucket_name = 'bucket-desafio-vitor'
file_name = 'VendasTesouroDireto.csv'

s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket_name, Key=file_name)
csv_data = obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_data), sep=';')

# 4.1 Filtrar dados com dois operadores lógicos
df_filtrado = df[(df['PU'] > 1000) & (df['Quantidade'] < 50)]
print("\nFiltrando dados onde PU > 1000 e Quantidade < 50:\n", df_filtrado)

# 4.2 Funções de agregação
media_pu = df['PU'].mean()
soma_valor = df['Valor'].sum()
print(f"\nMédia do PU: {media_pu}")
print(f"Soma do Valor: {soma_valor}")

# 4.3 Função Condicional
df['Categoria Valor'] = df['Valor'].apply(lambda x: 'Alto' if x > 100000 else 'Baixo')
print("\nAdicionando categoria 'Alto' ou 'Baixo' com base no Valor:\n", df[['Valor', 'Categoria Valor']])

# 4.4 Função de Conversão
df['Data Venda'] = pd.to_datetime(df['Data Venda'], format='%d/%m/%Y')
print("\nConvertendo a coluna 'Data Venda' para o formato datetime:\n", df[['Data Venda']].head())

# 4.5 Função de Data
df['Ano Venda'] = df['Data Venda'].dt.year
print("\nAdicionando coluna 'Ano Venda' com o ano de cada venda:\n", df[['Data Venda', 'Ano Venda']].head())

# 4.6 Função de String
df['Tipo Titulo'] = df['Tipo Titulo'].str.upper()
print("\nConvertendo 'Tipo Titulo' para maiúsculas:\n", df[['Tipo Titulo']].head())

# Salvar o resultado em um novo CSV
output_csv = 'C:\Users\Vitor\Documents\trabalho\PB-JOAO-VITOR-DE-MELO-REVOREDO\Sprint-5\Desafio\VendasTesouroDireto_modificado.csv'
df.to_csv(output_csv, index=False, sep=';')

# Carregar o arquivo modificado para o S3
s3.upload_file(output_csv, bucket_name, 'VendasTesouroDireto_modificado.csv')
print(f'Arquivo modificado carregado com sucesso para o bucket {bucket_name}.')
