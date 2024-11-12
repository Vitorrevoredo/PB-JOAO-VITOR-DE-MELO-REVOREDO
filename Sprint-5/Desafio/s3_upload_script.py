import boto3

# Configuração do cliente S3 com a região apropriada
s3 = boto3.client('s3', region_name='us-east-1')

# Definindo o nome do bucket e o nome do arquivo
bucket_name = 'bucket-desafio-vitor'
file_name = 'VendasTesouroDireto.csv'
file_path = 'C:/Users/Vitor/Documents/trabalho/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-5/Desafio/VendasTesouroDireto.csv'

# Tentando carregar o arquivo para o S3
s3.upload_file(file_path, bucket_name, file_name)
print(f'Arquivo {file_name} carregado com sucesso para o bucket {bucket_name}.')
    
