<h1>Desafio: Manipulação e tratamento de arquivo csv</h1>
<p>
  O objetivo desse desafio era ler e manipular o arquivo <code>googleplaystore.csv</code> utilizando python para analise de dados e 
  geração de gráficos. Todo código com suas respectivas saidas pode ser encontrado no arquivo <strong>Desafio.ipynb</strong> que exibe cada parte de forma estruturada.
</p>
<a href="/Sprint-3/Desafio/Desafio.ipynb">Arquivo ipynb</a> <br>
<h2>Passo a passo para resolução do Desafio</h2>
<ul>
<strong>Ferramenta e bibliotecas utilizadas respectivamente:</strong>
<Li><strong>Jupyter Lab</strong></Li>
<li><strong>Pandas</strong></li>
<li><strong>Matplotlib</strong> </li>
</ul>
<ol>
<h3>Leitura e remoção de duplicados do arquivo csv</h3>
<li>Comecei preparando o ambiente e importanto o arquivo csv para o Jupyter utilizando o Pandas, por meio do comando read_csv e armazenando
  em uma váriavel que chamei de df</li>
<img src="/Sprint-3/Evidencias/configurando_ambiente.png" width=500px>
  <li>Para remoção dos duplicados estava fazendo por meio do comando: <code>df.drop_duplicates()</code>, mas inicialmente 
  passar parametros, o que resultou em alguns erros na analise dos dados, pois a minima diferença não era levada em consideração para 
  retirar a duplicação, após as monitorias consegui entender que seria necessário fazer por App. 
  Resultando no ajuste <code>df = df.drop_duplicates(subset='App', keep='first')</code> </li>
  <strong>- Drop_duplicate sem parametros</strong> <br>
  <img src="/Sprint-3/Evidencias/drop_duplicate_sem_parametro.png" width=500px> <br>
  <strong> - Drop_duplicate com parametros</strong> <br>
  <img src="/Sprint-3/Evidencias/drop_duplicate_com_parametro.png" width=500px>
</ol>
<h3>Top 5 apps mais instalados</h3>
<ul>
  <li>Para encontrar os apps mais instalados tive que fazer o tratamento da coluna de <code>Installs</code> porque tinha dados que não
  eram númericos como <strong> ","-"+"-"Free"</strong> que não permitiam fazer a seleção, para não modificar o arquivo original, armazenei em uma
  variavel o tratamento dos dados da coluna. </li>
  <li>O <code>.str.replace</code> substitui as strings por espaços vazios ou troca por 0 e 
  depois o <code>.astype(float)</code> transforma em valores númericos, <code>df.nlargest(5, 'Installs')</code> seleciona os 5 apps 
   mais instalados após o tratamento da coluna Installs.
  </li>
  <img src="/Sprint-3/Evidencias/top_5_apps.png" width=500px>
</ul>
<h3>Gráfico top 5 apps</h3>
<p>Para elaborar o gráfico de barras, utilizei a biblioteca <code>Matplotlib</code> como recomendado:</p>
 <ul> 
   <li><code>plt.bar(top_5_apps['App'], top_5_apps['Installs']</code> cria o gráfico com base na váriavel;</li>
   <li><code>plt.xlabel('Nome do App')</code> e <code>plt.ylabel('Numeros de instalações')</code> colocam os labels no eixo X e Y do gráfico;</li>
   <li><code>plt.title('Top 5 Apps mais instalados')</code> insere o titulo;</li>
    <li> <code>plt.xticks(rotation = 90, ha='center')</code> ajusta a forma de exibição dos nomes na legenda; </li>
   <li>Para melhor visualização dos apps, resolvi criar uma coluna com as cores <code>cores = ['blue', 'yellow', 'green', 'red', 'purple']</code>para identificar melhor
     cada app e inserir no gráfico;</li>
   <li>Tambem coloquei como saida para salvar o gráfico em pdf antes da exibição com o 
     <code>plt.savefig('grafico_top5_apps_instalados.pdf', format='pdf', bbox_inches='tight')</code></li>
</li>
 </ul>
   <a href="/Sprint-3/Desafio/Graficos gerados/grafico_top5_apps_instalados.pdf">Gráfico top 5 em pdf</a> <br>
<strong>Exemplos de versões do top 5 apps e código utilizado</strong>
<img src="/Sprint-3/Evidencias/ajuste_cores_barra.png" width=500px>
<img src="/Sprint-3/Evidencias/mesmas_cores_barra.png" width=500px>
<img src="/Sprint-3/Evidencias/grafico_de_barras.png" width=500px>
<h3>Categorias presentes no Dataset</h3>
<ul>
  <li>Para separar o apps por categoria utilizei o <code>groupby</code> na Category e contando por totais números de instalações</li>
  <li> Na primeira versão a vizualização das categorias não ficaram boas pois muitas foram encontradas, para resolver, coloquei uma 
  categoria de Outros que levava como parametro um limite de apps com menos de 250 instalações, que permitiu gerar o top 15 categorias.</li>
    <li>
    As variáveis <strong>categorias_acima_limite</strong> e <strong>categorias_abaixo_limite</strong> ajustam e dividem corretamente as categorias em relação ao limite estabelecido.
 <li>Para criação do gráfico de pizza foram usados <code>plt.figure</code> e <code>plt.pie</code>, que criam e ajustam o gráfico com base nas variáveis.</li>
</ul>
<img src="/Sprint-3/Evidencias/erro_grafico_categorias.png" width="500px">
<img src="/Sprint-3/Evidencias/ajuste_grafico_pizza.png" width="500px">

<h3>App mais caro existente no Dataset</h3>
<ul>
  <li>Para fazer a análise do App mais caro, utilizei a mesma lógica de tratamento da coluna <code>Price</code>.</li>
  <li>Em seguida, usei o <code>loc</code> para encontrar o App mais caro pelo índice, com os comandos <code>precos_float.nlargest(1)</code> e <code>index</code>.</li>
</ul>
<strong>Exemplo de erro enfrentado no tratamento de dados e versão utilizada:</strong>
<img src="/Sprint-3/Evidencias/erro_tabela_app_caro.png" width="450px">
<img src="/Sprint-3/Evidencias/app_mais_caro.png" width="450px">

<h3>Contando quantos apps têm a classificação "Mature 17+"</h3>
<ul>
  <li>Realizei a soma das linhas equivalentes à string <code>"Mature 17+"</code> para encontrar o total.</li>
</ul>
<img src="/Sprint-3/Evidencias/mature17+.png" width="450px">

<h3>Top 10 Apps por reviews</h3>
<ul>
  <li>Para encontrar os apps, fiz a separação das colunas <strong>App</strong> e <strong>Reviews</strong>, ordenando pelos maiores valores. No entanto, enfrentei um erro, pois alguns valores estavam sendo tratados como strings, e não como números.</li>
<li>Para resolver, utilizei o comando <code>df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')</code>, que faz a conversão dos valores da coluna <strong>Reviews</strong> para tipos numéricos.</li>
</ul>
<strong> - Tabela sem tratamento</strong>
<img src="/Sprint-3/Evidencias/erro_top_10_apps.png" width="450px">
<strong> - Tabela corrigida</strong>
<img src="/Sprint-3/Evidencias/top_10_apps_reviews.png" width="450px"> <br>
<h3>Calculos que pensei com o Dataset</h3>
<strong>Média de Preço dos Apps por Categoria </strong>
<ul>
  <li>Utilizando o mesmo tipo de tratamento já exemplificado de mudar os dados da coluna <strong>Price</strong> e transformar os dados em um tipo númerico com o <code>to_numeric</code>.</li>
  <li>Adicionei uma coluna no df de Preço em float novamente e utilizei a função <code>.mean()</code> para gerar a média.</li>
</ul>
<img src="/Sprint-3/Evidencias/media_preco_categoria.png" width="450px">
<strong>Numero total de apps por categoria</strong>
<ul><li>Separei pela Categoria a soma da quantidade de apps</li></ul>
<img src="/Sprint-3/Evidencias/quantidade_apps_categoria.png" width="450px">
<strong>Média de preço de todos os Apps</strong>
<ul>Fazendo o tratamento da coluna de preço com <code>preco_tratado = df['Price'].str.replace('$', '').replace('Everyone', '0').astype(float)</code> e a média com o <code>.mean()</code></ul>
<img src="/Sprint-3/Evidencias/media_preco_todos_apps.png" width="500px">
<strong>App mais barato do Dataset</strong>
<ul>
  <li>Considerando os apps que não são gratuitos, ou seja, valores maiores que 0</li>
  <li>Fiz o tratamento das colunas e uma estrutura condicional que verifica se o valor é maior que 0, caso nenhum App seja encontrado, é retornada a mensagem <strong>"Não há aplicativos com preço diferente de zero"</strong></li>
</ul>
<img src="/Sprint-3/Evidencias/app_mais_barato.png" width="500"px>
