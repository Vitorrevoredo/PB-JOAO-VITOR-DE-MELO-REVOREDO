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

# Inspecionar as primeiras linhas do DataFrame
print("Primeiras linhas dos dados:")
print(df.head())

# Verificar o tipo de dados das colunas 'PU' e 'Quantidade'
print("\nTipos de dados das colunas antes de conversão:")
print(df.dtypes)

# Limpeza dos dados: converter 'PU', 'Quantidade' e 'Valor' para valores numéricos
df['PU'] = pd.to_numeric(df['PU'].str.replace(',', '.', regex=False), errors='coerce')
df['Quantidade'] = pd.to_numeric(df['Quantidade'].str.replace(',', '.', regex=False), errors='coerce')
df['Valor'] = pd.to_numeric(df['Valor'].str.replace(',', '.', regex=False), errors='coerce')

# Verificar novamente os tipos de dados
print("\nTipos de dados das colunas após conversão:")
print(df.dtypes)

# Verificar se há valores ausentes nas colunas 'PU' e 'Quantidade'
print("\nValores ausentes nas colunas 'PU' e 'Quantidade':")
print(df[['PU', 'Quantidade']].isnull().sum())

# Remover linhas com NaN nas colunas 'PU' e 'Quantidade'
df = df.dropna(subset=['PU', 'Quantidade'])

# Exibir estatísticas para garantir que os valores foram tratados corretamente
print("\nEstatísticas após tratamento de dados:")
print(df[['PU', 'Quantidade', 'Valor']].describe())

# Filtrando dados onde PU > 1000 e Quantidade < 50
df_filtrado = df[(df['PU'] > 1000) & (df['Quantidade'] < 50)]
print("\nFiltrando dados onde PU > 1000 e Quantidade < 50:\n", df_filtrado)

# Cálculos de média e soma
media_pu = df_filtrado['PU'].mean() if not df_filtrado.empty else 0
soma_valor = df_filtrado['Valor'].sum() if not df_filtrado.empty else 0
print(f"\nMédia do PU (filtrado): {media_pu}")
print(f"Soma do Valor (filtrado): {soma_valor}")

# Função Condicional para Categorizar 'Valor'
df['Categoria Valor'] = df['Valor'].apply(lambda x: 'Alto' if x > 100000 else 'Baixo')

# Conversão de 'Data Venda' e extração de 'Ano Venda'
df['Data Venda'] = pd.to_datetime(df['Data Venda'], format='%d/%m/%Y', errors='coerce')
df['Ano Venda'] = df['Data Venda'].dt.year

# Conversão de 'Tipo Titulo' para maiúsculas
df['Tipo Titulo'] = df['Tipo Titulo'].str.upper()

# Salvar o DataFrame modificado em um novo CSV
df.to_csv(output_file, index=False, sep=';')

# Carregar o arquivo modificado para o S3
s3.upload_file(output_file, bucket_name, 'VendasTesouroDireto_modificado.csv')
print(f'Arquivo modificado carregado com sucesso para o bucket {bucket_name}.')
