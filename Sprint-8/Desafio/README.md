<h1>Desafio da Sprint 8 - Processamento da Camada Trusted</h1>
<p>Esta sprint teve como foco principal o processamento e a padronização dos dados para a camada Trusted do Data Lake. O objetivo foi garantir que os dados provenientes da camada Raw estivessem confiáveis e organizados, utilizando Apache Spark para leituras, validações e gravações em formato PARQUET na Trusted Zone.</p>

<p>As principais ferramentas e tecnologias utilizadas nesta sprint foram:</p>
<ul>
  <li><strong>AWS Glue:</strong> Processamento de dados em larga escala e transformações.</li>
  <li><strong>Amazon S3:</strong> Armazenamento e gerenciamento dos arquivos processados.</li>
  <li><strong>Amazon Athena:</strong> Consultas e validações dos dados salvos na camada Trusted.</li>
</ul>

<h2>Estrutura dos Dados</h2>
<p>O foco principal desta sprint foi nos arquivos CSV e JSON carregados anteriormente na camada Raw. Esses dados foram transformados e padronizados para a Trusted Zone.</p>

<h2>Critérios de Limpeza e Confiabilidade</h2>
<p>Como decidi focar minha análise em filmes dos gêneros Comédia e Animação, apliquei os seguintes critérios de limpeza para garantir maior confiabilidade nos dados:</p>
<ul>
  <li><strong>Verificação e remoção de linhas com campos incompletos ou inconsistentes:</strong>
    <ul>
      <li>Linhas com valores nulos (\N ou vazios).</li>
      <li>Campos importantes, como <code>id</code>, <code>tituloPrincipal</code> e <code>anoLancamento</code>, foram considerados obrigatórios.</li>
    </ul>
  </li>
  <li><strong>Validação e padronização de campos específicos:</strong>
    <ul>
      <li>Confirmar que <code>anoLancamento</code> tem apenas números válidos.</li>
      <li>Garantir que <code>genero</code> esteja categorizado corretamente.</li>
    </ul>
  </li>
  <li><strong>Filtragem e ajuste de dados sobre pessoas e personagens:</strong>
    <ul>
      <li>Verificar se campos como <code>anoNascimento</code> ou <code>anoFalecimento</code> fazem sentido e padronizar o formato, removendo valores inválidos (\N).</li>
    </ul>
  </li>
</ul>

<h2>Passo a Passo do Desafio</h2>
<p>Comecei reexecutando a função Lambda para trazer os dados atualizados para o TMDB:</p>
<img src="../Evidencias/reexecução_lamda.png" alt="Reexecução Lambda">
<p>Para o processamento, comecei configurando o job para o arquivo CSV:</p>
<img src="../Evidencias/configurando_job_csv.png" width="500px" alt="Lendo arquivos CSV"> 
<p>Fui realizando os ajustes até chegar na versão final do código: <br>
<a href="../Desafio/processamento_csv.py">Processamento CSV</a></p>
<p>Por fim, os dados foram gravados na camada Trusted:</p>
<img src="../Evidencias/evidencia_execução_csv.png" width="500px" alt="Resultado execução do CSV"> 
<p>Para os arquivos JSON:</p>
<img src="../Evidencias/configurando_job_json.png" width="500px" alt="Configurando Job JSON"> 
<p>Apliquei os mesmos princípios de limpeza, focando nos critérios específicos para esse formato de arquivo:</p>
<a href="../Desafio/processamento_tmdb.py">Processamento TMDB</a>
<p>Os dados limpos também foram salvos na camada Trusted em formato PARQUET:</p>
<img src="../Evidencias/evidencia_execução_tmdb.png" width="500px" alt="Gravando dados JSON"> 

<h2>Evidências</h2>
<p>A estrutura dos dados no Amazon S3 foi mantida conforme planejado, com particionamento baseado na data de processamento:</p>
<pre><code>s3://vitor-data-lake/Trusted/PARQUET/&lt;arquivo&gt;/&lt;ano&gt;/&lt;mês&gt;/&lt;dia&gt;</code></pre>
<img src="../Evidencias/path_csv.png" width="500px" alt="Evidência da estrutura Trusted Zone CSV">
<img src="../Evidencias/path_tmdb.png" width="500px" alt="Evidência da estrutura Trusted Zone JSON">  
<p>Em seguida, criei um crawler para persistir os dados no Catálogo do Glue e o executei:</p>
<img src="../Evidencias/crawler_criado.png" alt="Crawler Criado">
<img src="../Evidencias/crawler_executado.png" alt="Executando crawler">
<p>Tabelas criadas:</p>
<img src="../Evidencias/tabelas_data_catalog.png" alt="Tabelas no Glue Catalog">
<p>Realizei alguns testes de pesquisa no Athena:</p>
<img src="../Evidencias/executando_athena.png" alt="Executando AWS Athena">
<p>Obtive os seguintes resultados:</p>
<img src="../Evidencias/resultado_athena.png" alt="Exemplo de resultado no Athena">

<h2>Conclusão</h2>
<p>Essa etapa foi fundamental para garantir que os dados disponíveis na Trusted Zone estejam confiáveis, organizados e prontos para as próximas etapas de análise. A limpeza e padronização aplicadas ajudam a manter a qualidade e a eficiência nos processos futuros do projeto.</p>
