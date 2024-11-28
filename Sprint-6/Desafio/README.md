<h1>Desafio do S3 com Python</h1>  
<p>Este projeto é dividido em cinco etapas, sendo a primeira focada no envio automatizado de dois arquivos CSV (Filmes e Séries) para um bucket na AWS S3. Além disso, foram levantadas perguntas para análise futura dos dados.</p>  

<ul>  
  <p>As principais ferramentas utilizadas foram:</p>  
  <li><strong>AWS S3:</strong> Armazenamento e gerenciamento dos arquivos no Data Lake.</li>  
  <li><strong>Python (bibliotecas):</strong></li>  
  <ul>
    <li><strong>Boto3:</strong> Interação com os serviços da AWS.</li>  
    <li><strong>OS:</strong> Manipulação de caminhos de arquivos.</li>  
    <li><strong>Dotenv:</strong> Carregamento de variáveis de ambiente a partir de arquivos .env.</li>  
  </ul>
</ul>  

<h2>Estrutura dos Dados</h2>  
<strong>Filmes:</strong> Contém informações como título, gênero, data de lançamento e personagens.<br>  
<strong>Séries:</strong> Similar aos filmes, mas com dados específicos de séries de TV.  

<h2>Perguntas para Análise dos Dados</h2>  
<ol>  
  <li>Quais artistas (atores ou diretores) têm mais obras conhecidas nos gêneros Comédia e Animação?</li>  
  <li>Quais anos apresentaram o maior número de lançamentos em comédia e animação?</li>  
  <li>Quais filmes ou séries de comédia e animação têm o maior número de votos em relação à nota média?</li>  
  <li>Qual é o tempo médio de duração de filmes de comédia em comparação com animações?</li>  
</ol>  

<h2>Credenciais AWS</h2>  
<p>Para proteger as credenciais de acesso à AWS, utilizei um arquivo .env, que armazena variáveis de ambiente de forma segura. Essa abordagem evita que as credenciais sejam incluídas diretamente no código-fonte, reduzindo o risco de exposição. Também utilizei o .gitignore para evitar que essas informações sejam publicadas no GitHub.</p>  

<img src="../Evidencias/git_ignore_credenciais.png" width="500px" alt="Credenciais AWS">  
<a href="/Sprint-6/Desafio/.env.example">Exemplo da estrutura do .env</a>  

<h2>Passo a Passo para Resolução do Desafio</h2>  
<p>Comecei criando o bucket no S3 para armazenar os arquivos:</p>  
<img src="../Evidencias/criando_bucket_s3.png" width="500px" alt="Criando bucket S3">  
<p>Configurei uma role de acesso ao bucket para permitir o acesso:</p>  
<img src="../Evidencias/permissoes_buckets3.png" width="500px" alt="Permissões de acesso ao bucket S3">  

<p>Em seguida, criei o script em Python para fazer o upload dos arquivos:</p>  
<p>O script carrega variáveis de ambiente utilizando o arquivo <strong>.env</strong>. Ele interage com o S3 via boto3 e cria uma estrutura hierárquica de pastas baseada na data atual (formato ano/mês/dia). O envio dos arquivos movies.csv e series.csv foi testado inicialmente sem o Docker para ajustes e validações.</p>  

<img src="../Evidencias/arquivo_upload_testes.png" width="500px" alt="Arquivo upload teste">  
<p>Configurei um ambiente de teste com o AWS CLI para validar o envio do script:</p>  
<img src="../Evidencias/config_aws_cli_teste.png" width="500px" alt="Configuração AWS CLI">  
<img src="../Evidencias/data_lake_depois_teste.png" width="500px" alt="Data Lake após teste">  
<p>O script automatiza o envio de arquivos para o AWS S3, organizando-os de acordo com a data atual. Ele faz uso das bibliotecas Python para garantir uma integração segura e eficiente.</p>  
<img src="../Evidencias/teste_executado.png" width="500px" alt="Teste executado">  
<p><strong>Após os testes, excluí os arquivos e preparei o ambiente para criação do Dockerfile.</strong></p>  
<img src="../Evidencias/excluindo_teste.png" width="500px" alt="Excluindo arquivos de teste">  

<p>Link para o script:</p>  
<ul>  
  <li><a href="./Sprint-6/Desafio/upload_s3.py">Script Python</a></li>  
</ul>  

<h2>Dockerfile</h2>  
<p>O Dockerfile foi configurado para criar o ambiente Python, instalar as dependências necessárias e executar o script Python para enviar os arquivos para o S3.</p>  
<img src="../Evidencias/config_dockerfile.png" width="500px" alt="Dockerfile">  

<ul>  
  <li><strong>Imagem Base:</strong> Usa a imagem oficial do Python 3.9.</li>  
  <li><strong>Diretório de Trabalho:</strong> Define o diretório /app onde os arquivos serão copiados.</li>  
  <li><strong>Instalação de Dependências:</strong> Instala as bibliotecas boto3, pandas e python-dotenv.</li>  
  <li><strong>Execução do Script:</strong> Define o comando para rodar o script Python upload_s3.py.</li>  
</ul>  

<h2>Comandos de Execução do Docker</h2>  
<p>Criando a imagem Docker:</p>  
<pre><code>docker build -t vitor-docker .</code></pre>  

<p>O comando para executar o container Docker. O arquivo .env é passado como parâmetro para garantir que as variáveis de ambiente sejam carregadas corretamente:</p>  
<img src="../Evidencias/criando_imagem_docker.png" width="500px" alt="Criando imagem Docker">  
<pre><code>docker run -it --env-file C:\Users\Vitor\Documents\Vitor\PB-JOAO-VITOR-DE-MELO-REVOREDO\Sprint-6\Desafio\.env -v C:\Users\Vitor\Documents\Vitor\PB-JOAO-VITOR-DE-MELO-REVOREDO\Sprint-6\Desafio:/app vitor-docker</code></pre>  

<p>Exemplo de erro encontrado:</p>  
<img src="../Evidencias/erro_docker.png" width="500px" alt="Exemplo de erro no Docker">  

<h2>Conclusão</h2>  
<p>Este projeto foi de grande importância para entender como utilizar o AWS S3 para criar e gerenciar um Data Lake. O uso do Docker possibilitou criar um ambiente isolado e portátil, garantindo que o código Python fosse executado de maneira consistente. Isso facilita o armazenamento e a análise de grandes conjuntos de dados no futuro.</p>  
