<h1>Desafio: Normalização da Tabela e Modelagens Dimensionais e Relacionais</h1> 

<p>O objetivo deste desafio era normalizar uma tabela de uma concessionária, aplicando as 3 Formas Normais (1FN, 2FN, 3FN) à sua estrutura, e, a partir disso, transformar o modelo relacional existente em um modelo dimensional. Isso permitiu a criação de consultas eficientes para análise de dados e relatórios.</p>

<h2>Normalização</h2> 

<ul>
  <li><strong>Redundância de dados:</strong> A tabela original tinha informações desorganizadas, o que aumentava o risco de erros e inconsistências. Isso foi resolvido pela criação de dimensões específicas.</li>
  <li><strong>Consultas ineficientes:</strong> A falta de organização dificultava a execução de consultas complexas. Passei por varias versões que exibi melhor no tópico <strong>Versões das modelagens</strong>, e a cada versão o desempenho das consultas e relações foi melhorado.</li>
</ul>

<h2>Passo a Passo para Resolução do Desafio</h2>

<ol>
  <li><strong>Entendimento da Estrutura Original:</strong> A tabela original de locações (<code>tb_locacao</code>) incluía informações redundantes sobre clientes, carros, vendedores e locacões, mas de maneira desorganizada. O primeiro passo foi identificar as entidades principais para criar um modelo relacional mais robusto.</li>
  <li><strong>Normalização (1FN, 2FN, 3FN):</strong> Dividi as informações em tabelas menores (dimensões), cada uma focada em uma entidade (Cliente, Carro, Vendedor, Combustível) e percebi que era necessário criar uma <code>locacao</code>, que seria utilizada para armazenar todas as informações de vendas no período, funcionando como uma tabela fato do modelo relacional. Coloquei cada ID das tabelas como <code>FOREIGN KEY</code> na criação das relações.</li>
</ol>
<h2> Arquivo da Normalização</h2>
<p>Para detalhar melhor os comandos SQL utilizados na normalização e criação das tabelas, fiz um arquivo como solicitado que descreve a lógica de aplicação das Formas Normais, assim como um diretório com os scripts de criação das tabelas relacionais:</p>
  <li><a href="/Sprint-2/Desafio/FormasNormais.sql">Formas Normais e Normalização</a></li>

<p>A ferramenta que usei foi o <strong>DBeaver</strong> para executar os comandos SQL e verificar o funcionamento da normalização. As tabelas criadas foram:</p>
<ul>
  <li><strong>Clientes</strong></li>
  <li><strong>Carros</strong></li>
  <li><strong>Vendedores</strong></li>
  <li><strong>Combustível</strong></li>
  <li><strong>locacao</strong></li>
</ul>

<p>Para criação das tabelas usei o CREATE TABLE com os respectivos valores das colunas e inseri os dados com o SELECT DISTINC e permitindo gerar as dimensões com os dados distindo e correto que permitiram a eliminação da duplicidade de dados e facilitaram a manutenção futura. O foco foi garantir que os dados fossem organizados de forma eficiente e atendessem às <strong>Três Formas Normais</strong>.</p>

<strong> Evidências da Normalização e criação das relações:</strong> Abaixo estão imagens que mostram etapas da criação das tabelas e ajustes das relações:</li>

<img src="/Sprint-2/Evidencias/criação-tabela-clientes-nf2.png" width="450px" alt="Criação da Tabela de Clientes NF2">
<img src="/Sprint-2/Evidencias/inserindo-dados-tbclientes.png" width="450px" alt="Inserindo Dados na Tabela de Clientes">
<img src="/Sprint-2/Evidencias/cr-tb-carros.png" width="450px" alt="Criação da Tabela de Carros">
<img src="/Sprint-2/Evidencias/ajuste-tbcarros.png" width="450px" alt="Ajuste na Tabela de Carros">

<p>Para solucionar os erros nas relações, utilizei <code>FOREIGN KEY</code> para estabelecer as dependências corretas entre as tabelas, conforme mostrado nas imagens abaixo:</p>

<img src="/Sprint-2/Evidencias/ajuste-relacao-tabelas.png" width="350px" alt="Ajuste de Relação entre as Tabelas">
<img src="/Sprint-2/Evidencias/evidencia-ajuste-relacao.png" width="350px" alt="Evidência do Ajuste de Relação entre as Tabelas">
<strong>Ao finalizar a modelagem relacional fiz o drop da tb_locacao</strong>
  <img src="/Sprint-2/Evidencias/drop_tb_locacao.png" width="400px">

<h2> Arquivos das Tabelas Criadas</h2>
  <li><a href="/Sprint-2/Desafio/tabelas-relacionais">Tabelas Relacionais Usadas</a></li>
<strong> - MODELO RELACIONAL GERADO</strong>
<img src="/Sprint-2/Desafio/modelo_relacional.png" width="400px" alt="Modelo Relacional gerado">

<h3>Modelagem Dimensional</h3> 

<p>Na segunda etapa, converti o modelo relacional em um modelo dimensional (e acredito que minha maior dificuldade). Nas versões o modelo foi estruturado com a criação de <code>views</code> para cada dimensão: Cliente, Carro, Vendedor, Tempo e Combustível, e a fato que unia todas as dimensões. </p>

<p> Para fazer as views e dimensão fato comecei desmembrando o modelo relacional em diferentes áreas!
As views criadas foram:</p>
<ul>
  <li><strong>Clientes</strong></li>
  <li><strong>Carros</strong></li>
  <li><strong>Vendedores</strong></li>
  <li><strong>Combustível</strong></li>
  <li><strong>Tempo</strong></li>
  <li><strong>Fato</strong></li>
</ul>

<h2>Exemplo de versão de criação dos diretorio e das views</h2>

<img src="/Sprint-2/Evidencias/ev-criação-views.png" width="400px" alt="Criação das Views">
<img src="/Sprint-2/Evidencias/testeviews.png" width="400px" alt="Teste das Views">

<h2> Arquivos das Views Criadas</h2>
<a href="/Sprint-2/Desafio/Views/">Views Utilizadas</a>
<br>
<strong> - MODELO DIMENSIONAL GERADO</strong>
<br>
<img src="/Sprint-2/Desafio/modelo_dimensional.png" width="400px" alt="Modelo Dimensional gerado">

<h2>Perguntas</h2>

<strong> Exemplos de algumas perguntas que pensei que poderia responder com a Tabela Fato e as Dimensões:</strong>
<ul>
  <li>Qual vendedor fez o maior valor de locações no período? 
    <br>
    <img src="/Sprint-2/Evidencias/primeira_pergunta_dim.png" width="500px" alt="Query da primeira pergunta e resultado">
    <br>
  <strong> Unindo a fato de locações (vw_fatos_locacao) com a dimensão de vendedores (vw_dim_vendedor) através do idVendedor. A soma de vlrTotal nos dá o valor total das vendas de cada vendedor, e a ordenação mostra quem fez o maior valor de locações.</strong></li>
  <li>Qual foi o total de locações para um tipo de combustível específico? 
    <br>
    <img src="/Sprint-2/Evidencias/segunda_pergunta_dim.png" width="500px" alt="Query da segunda pergunta e resultado">
    <br>
  <strong>Com a fato de locações (vw_fatos_locacao) unindo com a dimensão de combustível (vw_dim_combustivel) pelo idcombustivel. Isso permite contar quantas locações foram feitas para carros que utilizam um tipo de combustível específico (como 'Gasolina').</strong></li>
  <li>Qual o valor médio das locações de carros de uma determinada marca?
    <br>
    <img src="/Sprint-2/Evidencias/terceira_pergunta_dim.png" width="500px" alt="Query da terceira pergunta e resultado">
    <br>
  <strong>Unindo a locacao fato com adimensão de carros (vw_dim_carro) usando o idCarro. Isso nos permite calcular a média do valor das diárias para carros de uma marca específica (exemplo: 'Toyota').</strong></li>
</ul>




<strong>A tabela fato  de (<code>locacao</code>) foi projetada para armazenar métricas como quantidade de diárias total e valor Diarias, e varias outras podem ser geradas com base nas relações das dimensões.</strong>

<h3>Versões das modelagens </h3>
<p>Aqui estão alguns exemplos de modelos utilizados durante as versões da modelagem da <code>tb_locacao</code> que sofreram muitas alterações durante o processo, sendo a última a versão final do projeto:</p>

<img src="/Sprint-2/Evidencias/modelagemv1.png" alt="Modelo Versão 1" width="300px">
<img src="/Sprint-2/Evidencias/modelagemv2.png" alt="Modelo Versão 2" width="300px" >
<img src="/Sprint-2/Evidencias/modelagemv3.png" alt="Modelo Versão 3" width="300px">
<img src="/Sprint-2/Evidencias/modelo_relacionalv4.png" alt="Modelo Versão 4" width="300px">
<img src="/Sprint-2/Evidencias/modelos_finais.png" alt="Modelo Final" width="300px">

<h2> Comentários Finais </h2>
O desafio foi concluído com sucesso ao normalizar a tabela de locações e transformar o modelo relacional em dimensional. Através das etapas de normalização e da criação de dimensões e tabela fato, foi possível otimizar consultas e eliminar redundâncias, garantindo a integridade e eficiência dos dados para análises futuras.
