<h1>Desafio: Normalização da Tabela e Modelagens Dimensionais e Relacionais</h1> 

<p>O objetivo deste desafio era normalizar uma tabela de uma concessionária, aplicando as 3 Formas Normais (1FN, 2FN, 3FN) à sua estrutura, e, a partir disso, transformar o modelo relacional existente em um modelo dimensional. Isso permitiu a criação de consultas eficientes para análise de dados e relatórios.</p>
<strong> - MODELO RELACIONAL GERADO</strong>
<img src="/Sprint-2/Desafio/modelo_relacional.png" width="400px" alt="Modelo Relacional gerado">
<strong> - MODELO DIMENSIONAL GERADO</strong>
<img src="/Sprint-2/Desafio/modelo_dimensional.png" width="400px" alt="Modelo Dimensional gerado">

<h2>Normalização</h2> 

<ul>
  <li><strong>Redundância de dados:</strong> A tabela original tinha informações desorganizadas, o que aumentava o risco de erros e inconsistências. Isso foi resolvido pela criação de dimensões específicas.</li>
  <li><strong>Consultas ineficientes:</strong> A falta de organização dificultava a execução de consultas complexas. Após a normalização e a criação do modelo dimensional, o desempenho das consultas foi melhorado.</li>
</ul>

<ol>
  <li><strong>Entendimento da Estrutura Original:</strong> A tabela original de locações (<code>tb_locacao</code>) incluía informações redundantes sobre clientes, carros, vendedores e combustíveis. O primeiro passo foi identificar as entidades principais para criar um modelo relacional mais robusto.</li>
  <li><strong>Normalização (1FN, 2FN, 3FN):</strong> Dividi as informações em tabelas menores (dimensões), cada uma focada em uma entidade (Cliente, Carro, Vendedor, Combustível) e percebi que era necessário criar uma <code>info_locacoes</code>, que seria utilizada para armazenar todas as informações de vendas num período, funcionando como uma tabela fato do modelo relacional. Coloquei cada ID das tabelas como <code>FOREIGN KEY</code> na criação das relações.</li>
</ol>
<h2>Passo a Passo para Resolução do Desafio</h2> 

<p>A abordagem que utilizei foi com o auxílio da ferramenta <strong>DBeaver</strong> para executar os comandos SQL e verificar o funcionamento da normalização. O desafio exigiu a separação de dados em tabelas distintas para eliminar redundâncias e melhorar a integridade dos dados. As tabelas criadas foram:</p>
<ul>
  <li><strong>Clientes</strong></li>
  <li><strong>Carros</strong></li>
  <li><strong>Vendedores</strong></li>
  <li><strong>Combustível</strong></li>
  <li><strong>info_locacoes</strong></li>
</ul>

<p>Essas dimensões permitiram a eliminação da duplicidade de dados e facilitaram a manutenção futura. O foco foi garantir que os dados fossem organizados de forma eficiente e atendessem às <strong>Três Formas Normais</strong>.</p>

<strong> Evidências da Normalização e criação das relações:</strong> Abaixo estão imagens que mostram a criação das tabelas e ajustes das relações:</li>

<img src="/Sprint-2/Evidencias/criação-tabela-clientes-nf2.png" width="400px" alt="Criação da Tabela de Clientes NF2">
<img src="/Sprint-2/Evidencias/inserindo-dados-tbclientes.png" width="400px" alt="Inserindo Dados na Tabela de Clientes">
<img src="/Sprint-2/Evidencias/cr-tb-carros.png" width="400px" alt="Criação da Tabela de Carros">
<img src="/Sprint-2/Evidencias/ajuste-tbcarros.png" width="400px" alt="Ajuste na Tabela de Carros">

<p>Para solucionar os erros nas relações, utilizei <code>FOREIGN KEY</code> para estabelecer as dependências corretas entre as tabelas, conforme mostrado nas imagens abaixo:</p>

<img src="/Sprint-2/Evidencias/ajuste-relacao-tabelas.png" width="350px" alt="Ajuste de Relação entre as Tabelas">
<img src="/Sprint-2/Evidencias/evidencia-ajuste-relacao.png" width="350px" alt="Evidência do Ajuste de Relação entre as Tabelas">

<p>Para detalhar melhor os comandos SQL utilizados na normalização e criação das tabelas, fiz um arquivo como solicitado que descreve a lógica de aplicação das Formas Normais, assim como um diretório com os scripts de criação das tabelas relacionais:</p>

<h2> Arquivos das Formas Normais</h2>
  <li><a href="/Sprint-2/Desafio/FormasNormais.sql">Formas Normais e Normalização</a></li>
<h2> Arquivos das Tabelas Criadas</h2>
  <li><a href="/Sprint-2/Desafio/tabelas-relacionais">Tabelas Relacionais Usadas</a></li>


<h3>Modelagem Dimensional</h3> 

<p>Na segunda etapa, converti o modelo relacional em um modelo dimensional. O modelo foi estruturado com a criação de <code>views</code> para cada dimensão: Cliente, Carro, Vendedor, Tempo e Combustível. A tabela fato (<code>vw_fatos_locacao</code>) foi projetada para armazenar métricas como quantidade de diárias e valor total.</p>

<h2>Perguntas</h2>

<p>Aqui estão algumas perguntas que podem ser respondidas com a Tabela Fato e as Dimensões:</p>

<ol>
  <li><strong>Qual é o valor total de locações por vendedor?</strong> Usa a Dimensão Vendedor e a Tabela Fato para calcular a soma dos valores das locações por vendedor.</li>
  <li><strong>Quantas diárias foram feitas para cada cliente em determinado período?</strong> Usa a Dimensão Cliente e a Dimensão Tempo para agregar o total de diárias por cliente.</li>
  <li><strong>Qual o carro mais alugado e qual seu tipo de combustível?</strong> Usa a Dimensão Carro e a Dimensão Combustível para identificar os carros mais alugados e seus respectivos tipos de combustível.</li>
  <li><strong>Qual foi o valor total gerado pelas locações em um determinado período?</strong> Usa a Dimensão Tempo e a Tabela Fato para calcular o valor total das locações em um intervalo de tempo.</li>
  <li><strong>Qual a média de valor de diárias por carro?</strong> Usa a Dimensão Carro e a Tabela Fato para calcular a média do valor das diárias por modelo de carro.</li>
</ol>

<h2>Exemplo de criação das e diretorio das views</h2>

<img src="/Sprint-2/Evidencias/ev-criação-views.png" width="400px" alt="Criação das Views">
<img src="/Sprint-2/Evidencias/testeviews.png" width="400px" alt="Teste das Views">

<h2> Arquivos das Views Criadas</h2>
<li><a href="/Sprint-2/Desafio/views/">Views Utilizadas</a></li>

<h3>Versões dos modelos</h3>
<p>Aqui estão alguns exemplos de modelos utilizados durante as versões da modelagem da <code>tb_locacao</code> que sofreram muitas alterações durante o processo, sendo a última a versão final do projeto:</p>

<img src="/Sprint-2/Evidencias/modelagemv1.png" alt="Modelo Versão 1" width="300px" alt="Versão 1 modelagem">
<img src="/Sprint-2/Evidencias/modelagemv2.png" alt="Modelo Versão 2" width="300px" alt="Versão 2 modelagem">
<img src="/Sprint-2/Evidencias/modelagemv3.png" alt="Modelo Versão 3" width="300px" alt="Versão 3 modelagem">
<img src="/Sprint-2/Evidencias/"

<h2> Comentários Finais </h2>
O desafio foi concluído com sucesso ao normalizar a tabela de locações e transformar o modelo relacional em dimensional. Através das etapas de normalização e da criação de dimensões e tabela fato, foi possível otimizar consultas e eliminar redundâncias, garantindo a integridade e eficiência dos dados para análises futuras.
