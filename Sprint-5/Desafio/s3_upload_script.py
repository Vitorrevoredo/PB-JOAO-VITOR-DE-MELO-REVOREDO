import boto3

# Configuração do cliente S3 com a região apropriada
client = boto3.client('s3', region_name='us-east-1')

# Definindo o nome do bucket e o caminho do arquivo local
bucket_name = 'bucket-desafio-vitor'
file_name = 'VendasTesouroDireto.csv'
file_path = 'C:/Users/Vitor/Documents/trabalho/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-5/Desafio/VendasTesouroDireto.csv'

# Carregando o arquivo para o S3
client.upload_file(file_path, bucket_name, file_name)
print(f'Arquivo {file_name} carregado com sucesso para o bucket {bucket_name}.')
