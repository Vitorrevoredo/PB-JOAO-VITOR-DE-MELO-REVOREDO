<h1>Desafio da Sprint 8 - Processamento da Camada Trusted</h1>
<p>O objetivo desta sprint foi processar e padronizar os dados para a camada Trusted do Data Lake, garantindo que os dados provenientes da camada Raw fossem confiáveis e organizados. Utilizei o Apache Spark para realizar leituras, validações e gravações em formato PARQUET na Trusted Zone, considerando a estrutura do sistema de particionamento do Amazon S3 e as práticas recomendadas para processamento de grandes volumes de dados.</p>

<h2>Ferramentas e Tecnologias</h2>
<p>As ferramentas e tecnologias utilizadas para garantir o processamento eficiente e a padronização dos dados foram:</p>
<ul>
  <li><strong>AWS Glue:</strong> Para processamento de dados em larga escala e transformação de dados de várias fontes.</li>
  <li><strong>Amazon S3:</strong> Para o armazenamento dos dados processados, com particionamento por data de processamento.</li>
  <li><strong>Amazon Athena:</strong> Para consultas e validações de dados processados e armazenados na camada Trusted.</li>
  <li><strong>Apache Spark:</strong> Para realizar o processamento dos dados em paralelo no AWS Glue.</li>
</ul>

<h2>Processamento e Padronização dos Dados</h2>
<p>O foco desta sprint foi processar os dados já presentes na camada Raw (CSV e JSON), garantindo que estivessem confiáveis e organizados. Os seguintes critérios de limpeza e transformação foram aplicados para os dois formatos:</p>
<ul>
  <li><strong>Verificação e Remoção de Dados Inconsistentes:</strong>
    <ul>
      <li>Remoção de linhas com valores nulos ou inválidos em campos essenciais como <code>id</code>, <code>tituloPrincipal</code> e <code>anoLancamento</code>.</li>
    </ul>
  </li>
  <li><strong>Padronização de Campos:</strong>
    <ul>
      <li>Padronização do formato dos campos <code>anoLancamento</code> (apenas números válidos) e <code>genero</code> (categorias corretas de gênero).</li>
    </ul>
  </li>
  <li><strong>Ajuste nos Campos de Pessoas e Personagens:</strong>
    <ul>
      <li>Campos como <code>anoNascimento</code> e <code>anoFalecimento</code> foram validados e corrigidos, removendo valores inválidos (<code>\N</code>).</li>
    </ul>
  </li>
</ul>

<h2>Passo a Passo do Desafio</h2>
<p>Inicialmente, reexecutei a função Lambda para garantir que os dados do TMDB estivessem atualizados, como pode ser visto na imagem abaixo:</p>
<img src="../Evidencias/reexecução_lamda.png" alt="Reexecução Lambda">
<p>Para o processamento de arquivos CSV e JSON, configurei dois jobs no AWS Glue, um para cada formato. O processamento seguiu conforme o modelo apresentado abaixo. O código do processamento do arquivo CSV é detalhado aqui: <a href="../Desafio/processamento_csv.py">Processamento CSV</a>. O código do processamento do TMDB (JSON) pode ser conferido aqui: <a href="../Desafio/processamento_tmdb.py">Processamento TMDB</a>.</p>

<p>Após a execução bem-sucedida de cada job, os dados foram armazenados na camada Trusted do S3, utilizando o formato PARQUET, conforme os detalhes de particionamento por data de processamento:</p>
<img src="../Evidencias/evidencia_execução_csv.png" width="500px" alt="Resultado execução do CSV">
<img src="../Evidencias/evidencia_execução_tmdb.png" width="500px" alt="Gravando dados JSON">

<h2>Organização dos Dados no S3</h2>
<p>A estrutura de armazenamento foi cuidadosamente planejada para organizar os dados na Trusted Zone de maneira eficiente. Os dados foram particionados por ano, mês e dia de processamento, como mostrado abaixo:</p>
<pre><code>s3://vitor-data-lake/Trusted/PARQUET/&lt;arquivo&gt;/&lt;ano&gt;/&lt;mês&gt;/&lt;dia&gt;</code></pre>
<img src="../Evidencias/path_csv.png" width="500px" alt="Evidência da estrutura Trusted Zone CSV">
<img src="../Evidencias/path_tmdb.png" width="500px" alt="Evidência da estrutura Trusted Zone JSON">

<h2>Catalogação e Consultas no Athena</h2>
<p>Após gravar os dados no S3, utilizei um crawler do AWS Glue para registrar essas informações no Glue Catalog, facilitando o acesso por consultas do Athena:</p>
<img src="../Evidencias/crawler_criado.png" alt="Crawler Criado">
<img src="../Evidencias/crawler_executado.png" alt="Executando o crawler">
<p>As tabelas no Glue Catalog foram criadas com sucesso e puderam ser consultadas diretamente através do Amazon Athena para validação dos dados:</p>
<img src="../Evidencias/tabelas_data_catalog.png" alt="Tabelas no Glue Catalog">
<p>A consulta foi realizada para verificar a precisão dos dados e os resultados retornados pelo Athena são apresentados abaixo:</p>
<img src="../Evidencias/executando_athena.png" alt="Executando AWS Athena">
<img src="../Evidencias/resultado_athena.png" alt="Exemplo de resultado no Athena">

<h2>Conclusão</h2>
<p>Com a execução bem-sucedida desta etapa, garanti que os dados armazenados na camada Trusted estejam organizados, confiáveis e prontos para análise futura. A utilização do AWS Glue, Amazon S3, e Athena proporcionou uma solução escalável e eficiente para o processamento e consulta dos dados.</p>
