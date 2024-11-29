<h1>README - Sprint de Envio de Arquivos para o AWS S3 Utilizando Python e Docker</h1>

<h2>Instruções</h2>
<p>Esta Sprint tem como foco a automação do envio de arquivos para um bucket S3 utilizando Python e Docker, aplicando boas práticas de segurança e organização.</p>

<h2>Objetivos da Sprint</h2>
<ul>
  <li>Utilizar os serviços Aws</li>
  <li>Automatizar o envio de arquivos para o AWS S3.</li>
  <li>Utilizar Docker para criar um ambiente isolado e portátil.</li>
  <li>Garantir a segurança das credenciais com o uso de variáveis de ambiente.</li>
  <li>Realizar uma análise futura dos dados enviados.</li>
</ul>

<h2>Informações</h2>
<ul>
  <li><strong>Arquivos Enviados:</strong> Filmes e Séries (formato CSV).</li>
  <li><strong>Tecnologias Utilizadas:</strong> Python, Docker, AWS S3, AWS CLI.</li>
  <li><strong>Bibliotecas:</strong> Boto3, OS, Dotenv.</li>
</ul>

<h2>Anotações</h2>
<p>Durante o desenvolvimento, foi fundamental configurar corretamente o IAM e as políticas de acesso para garantir o acesso aos serviços AWS.</p>

<h2>Exercícios</h2>
<strong>Laboratorio Bucket s3</strong> 
<ul>
    <li>Criei meu bucket s3.</li>
  </ul>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/criação_bucket_s3.png" width="500px" alt="Criação do bucket s3">  
<strong> Em seguida fui fazer a configuração da hospedagem do site:</strong>
<ul>
      <li>Marquei a opção <strong>Use this bucket to host a website</strong>.</li>
      <li>Defini o <strong>Index document</strong> como <code>index.html</code>.</li>
      <li>(Opcional) Defini o <strong>Error document</strong> como <code>404.html</code>.</li>
  </ul>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/hospedagem_site_estatico.png" width="500px" alt="Hospedagem site"> 
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/erro_hospedagem_site_estatico.png" width="500px" alt="Hospedagem site erro"> 

<strong> Editando as Configurações de Bloqueio de Acesso Público:</strong> <br>
  <ul>
      <li>Desmarquei <strong>Block all public access</strong></li> <br>
  </ul>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/retirando_bloqueio_acesso.png" width="500px" alt="Hospedagem site erro resolvido"> <br>
<strong>Adicionando Política de Acesso Público ao Bucket:</strong> <br>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/politica_bucket.png" width="500px" alt="Hospedagem site erro resolvido"> <br>
<strong>Carreguei os arquivos para bucket:</strong> <br>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/carregando_arquivos.png" width="500px" alt="Carregando arquivos"> <br>
<strong>Site funcionando: </strong><br>
<img src="../Sprint-6/Exercicios/bucket s3 - evidencias/testando_endpoint.png" width="500px" alt="Hospedagem site erro resolvido"> <br>

<h2>Exercícios</h2>  
<strong>Laboratório AWS Athena</strong>  <br>
<strong>Analisando o Arquivo:</strong>  
<p>Baixei o arquivo <code>nomes.csv</code> e analisei as colunas para identificar o nome e o tipo de dado de cada uma.</p>  

<strong>Configurando o Athena:</strong>  
<ul>  
  <li>No Athena, fui até <strong>View Settings</strong> e selecionei <strong>Manage</strong>.</li>  
  <li>Inseri o caminho do bucket para armazenar os resultados das consultas, utilizando o prefixo <code>s3://</code> e apontando para a pasta</li>  
</ul>   <br>
<img src="../Sprint-6/Exercicios/athena - evidencias/localizacao_bucket_s3.png" width="500px" alt="Localização bucket s3">  <br>
<strong>Criando o Banco de Dados:</strong>  
<ul>  
  <li>No editor de consultas do Athena, inseri a seguinte instrução para criar o banco de dados:</li>  
</ul>   <br>

<img src="../Sprint-6/Exercicios/athena - evidencias/criando_banco_de_dados.png" width="500px" alt="Criando banco de dados"> 

<strong>Criando a Tabela:</strong>  
<pre><code>CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.minhatabela (
  nome STRING,
  ano INT,
  quantidade INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://seu-bucket/nomes.csv';</code></pre>  

<ul>  
  <li>Executei a query e verifiquei a mensagem <strong>Completed</strong> confirmando a criação da tabela.</li>  
</ul>  

<img src="../Sprint-6/Exercicios/athena - evidencias/criando_tabela.png" width="500px" alt="Criando tabela"> 

<strong>Testando os Dados:</strong>  
<ul>  
  <li>Rodei a seguinte consulta para listar os nomes mais populares em 1999:</li>  
</ul>  

<pre><code>SELECT nome FROM meubanco.minhatabela WHERE ano = 1999 ORDER BY quantidade DESC LIMIT 15;</code></pre>  

<img src="../Sprint-6/Exercicios/athena - evidencias/query_1.png" width="500px" alt="Query pesquisa">  <br>
<strong>Consulta Final:</strong>  
<p>Criei uma query para listar os três nomes mais usados em cada década desde 1950 até hoje.</p>
<img src="../Sprint-6/Exercicios/athena - evidencias/query_2.png" width="500px" alt="Query pesquisa 2"> 
<img src="../Sprint-6/Exercicios/athena - evidencias/excluindo_tabelas.png" width="500px" alt="Excluindo tabelas"> 
 
<strong>Laboratório AWS Lambda</strong>  
<strong>Criando a Função do Lambda:</strong>  
<img src="../Sprint-6/Exercicios/lambda - evidencias/criando_funcao_lambda.png" width="500px" alt="Criando função Lambda"> 

<strong>Construindo o Código:</strong>  
<ul> 
  <li>Substituí o código padrão pelo código que acessa o S3 e utiliza as bibliotecas Numpy e Pandas para realizar a operação. O código ficou assim:</li>  
</ul>  
<img src="../Sprint-6/Exercicios/lambda - evidencias/atualizando_função.png" width="500px" alt="Atualizando função Lambda"> 

<ul> 
  <li>Ao executar, o erro a seguir foi exibido:</li>  
</ul>  
<img src="../Sprint-6/Exercicios/lambda - evidencias/teste_erro.png" width="500px" alt="Teste erro"> 
<p>Este erro ocorreu pois o AWS Lambda não tem a biblioteca <code>pandas</code> instalada por padrão. Para resolver isso, precisamos adicionar uma camada (Layer) contendo a biblioteca <code>pandas</code>.</p>  

<strong>Criando uma Layer:</strong>  
<ul>    
  <li>Criei uma pasta nova e dentro dela criei um arquivo chamado <code>Dockerfile</code> com o seguinte conteúdo:</li>  
</ul>  
<img src="../Sprint-6/Exercicios/lambda - evidencias/criando_dockerfile.png" width="500px" alt="Dockerfile"> 

<ul>  
  <li>Com o <code>Dockerfile</code> pronto, criei a imagem do Docker utilizando o comando:</li>  
</ul>  
<img src="../Sprint-6/Exercicios/lambda - evidencias/criando_imagem_docker.png" width="500px" alt="Docker imagem"> 

<ul>  
  <li>Em seguida, executei o comando para acessar o shell do container:</li>  
</ul>  

<ul>  
  <li>Dentro do container, criei a estrutura de diretórios necessária para as bibliotecas:</li>  
</ul>  

<ul>  
  <li>Instalei as bibliotecas necessárias com o comando:</li>  
</ul>  

<pre><code>pip3 install pandas -t .
</code></pre>  

<ul>  
  <li>Com as bibliotecas instaladas, voltei para a pasta <code>layer_dir</code> e compactei tudo em um arquivo zip:</li>  
</ul>  

<pre><code>
bash-4.2# cd ..
bash-4.2# zip -r minha-camada-pandas.zip .
</code></pre>  

<ul>  
  <li>Copiei o arquivo zip do container para a minha máquina local utilizando o comando:</li>  
</ul>  

<img src="../Sprint-6/Exercicios/lambda - evidencias/copiando_zip.png" width="500px" alt="Copiando zip"> 

<ul>  
  <li>Com o arquivo <code>minha-camada-pandas.zip</code> na minha máquina local, fiz o upload dele para um bucket S3.</li>  
</ul>  

<img src="../Sprint-6/Exercicios/lambda - evidencias/upload_minha_camada_pandas.png" width="500px" alt="Upload camada zip"> 

<strong>Etapa 4: Utilizando a Layer</strong>  

<img src="../Sprint-6/Exercicios/lambda - evidencias/configurando_camadas.png" width="500px" alt="Configurando camada"> 
<p>
Durante uma Sprint anterior, encontrei um problema de acesso no AWS CLI e suspeitei que o erro de permissão estivesse relacionado ao IAM. Ao executar minha função Lambda, recebi a seguinte mensagem de erro:
</p>
<pre><strong>AccessDeniedException: User: arn:aws:sts::123456789012:assumed-role/role-name/lambda-function-name is not authorized to perform: s3:GetObject on resource: arn:aws:s3:::bucket-name</strong></pre>
<p>
Após uma pesquisa detalhada, descobri que a função estava configurada com a política padrão <code>AWSLambdaBasicExecutionRole</code>, que permite apenas gravar logs no CloudWatch, mas não acessar buckets S3.
</p>
<img src="../Sprint-6/Exercicios/lambda - evidencias/permissões_lambda.png" width="500px" alt="Permissão padrão Lambda"> 

<h2>Solução</h2>
<p>Para resolver o problema, segui os seguintes passos:</p>
<ol>
  <li>Acessei o console do <strong>IAM</strong>.</li>
  <li>Pesquisei pela função Lambda chamada <code>vitor-nomes</code>.</li>
  <li>Atribuí a role <strong>AmazonS3FullAccess</strong>, garantindo as permissões necessárias para acessar o bucket S3.</li>
</ol>
<img src="../Sprint-6/Exercicios/lambda - evidencias/mudando_permissões_iam.png" width="500px" alt="Mudando permissões no Iam">

<p>Após salvar as alterações, a função Lambda conseguiu acessar o bucket <code>exercicio-vitor</code> sem problemas,só precisei mudar as configurações de tempo de execução e memória</p>
<img src="../Sprint-6/Exercicios/lambda - evidencias/mudando_config_tempo_memoria.png" width="500px" alt="Configurações de execução">



<h2>Certificados</h2>
<p>Concluí cursos da AWS para aprimorar meu conhecimento nos serviços disponíveis na nuvem. Seguem os certificados em anexo:</p>
<ul>
  <li><a href="/Sprint-6/Certificados">Certificado AWS</a></li>
</ul>

<h2>Comentários Finais</h2>
<p>Esta Sprint foi essencial para entender a integração entre Python, Docker e AWS S3, além de reforçar a importância do controle de permissões no IAM para evitar problemas de acesso.</p>

