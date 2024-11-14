import pandas as pd
import boto3
from io import StringIO

# Configurações
bucket_name = 'bucket-desafio-vitor'
file_name = 'VendasTesouroDireto.csv'
output_file = 'C:/Users/Vitor/Documents/trabalho/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-5/Desafio/VendasTesouroDireto_modificado.csv'

# Conectando ao S3 e ler o arquivo
s3 = boto3.client('s3')
csv_data = s3.get_object(Bucket=bucket_name, Key=file_name)['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_data), sep=';')

# 4.1 Filtrando dados
df_filtrado = df[(df['PU'] > 1000) & (df['Quantidade'] < 50)]
print("\nFiltrando dados onde PU > 1000 e Quantidade < 50:\n", df_filtrado)

# 4.2 Funções de Agregações (Soma e Média) dos valores
print(f"\nMédia do PU: {df['PU'].mean()}")
print(f"Soma do Valor: {df['Valor'].sum()}")

# 4.3 Função Condicional
df['Categoria Valor'] = df['Valor'].apply(lambda x: 'Alto' if x > 100000 else 'Baixo')

# 4.4 e 4.5 Conversão e extração de ano
df['Data Venda'] = pd.to_datetime(df['Data Venda'], format='%d/%m/%Y')
df['Ano Venda'] = df['Data Venda'].dt.year

# 4.6 Função de String
df['Tipo Titulo'] = df['Tipo Titulo'].str.upper()

# Salvar e carregar para o S3
df.to_csv(output_file, index=False, sep=';')
s3.upload_file(output_file, bucket_name, 'VendasTesouroDireto_modificado.csv')
print(f'Arquivo modificado carregado com sucesso para o bucket {bucket_name}.')
