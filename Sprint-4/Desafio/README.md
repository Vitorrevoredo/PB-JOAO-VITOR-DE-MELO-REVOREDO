# Desafio: Utilização do Docker para criação de containers em arquivos python
## Arquivo carguru.py:
<p>Para resolução da etapa fiz o downloand do arquivo como solicitado e realizei os teste para ver qual era o output da aplicação, depois
de ver como funcionava parti para criação do Dockerfile para criação do container.</p>
<h2>Estrutura do Projeto</h2>
carguru.py: script Python responsável por gerar aleatoriamento um modelo de carro para saida e exibi-lo.
Dockerfile: arquivo de configuração para criação da imagem Docker. <br>
<strong>1. Script Python</strong>
<ul>
  <li>Utiliza a biblioteca <strong>random</strong> para selecionar um dado da lista <strong>carros</strong></li>
  <li>Gera o carros aletoriamento com o metodo <strong>.choice</strong></li>
  <li>Print da saida do carro com a frase</li>
</ul>
<strong>2. Criação da Imagem Docker</strong>
<strong>Arquivo Dockerfile</strong>
<p>Para criar a imagem Docker que executará o script Python, foi criado o Dockerfile com as seguintes instruções:</p>
<ul>
<strong>Base image</strong>
<li><code>FROM python</code></li>
<strong>Define o diretório de trabalho</strong>
<li><code>WORKDIR /app</code></li>
<strong>Copia o script Python para o container</strong>
<li><code>COPY carguru.py . </code></li>
<strong>Comando para executar o script Python</strong>
<li><code>CMD ["python", "carguru.py"] </code</li>
</ul>
<strong>Construção e Execução da Imagem Docker</strong>

