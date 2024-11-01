# Respostas sobre Containers Docker

## Pergunta 1: É possível reutilizar um container?

**Resposta:**  
Sim, é possível reutilizar um container parado. Para reiniciar um container parado, usamos o seguinte comando:

<code>docker start -i nome_do_container</code>

## Comandos utilizados para execução dos Containers
Logica dos comandos utilizados para construir e executar os containers:
Construção da Imagem:
docker build -t nome_da_imagem .
Execução do Container:
docker run --name nome_do_container nome_da_imagem
Reutilização dos containers:
docker start -i nome_do_container
Esses comandos permitem tanto a criação quanto a execução de containers, facilitando o desenvolvimento e a reutilização de imagens e containers.