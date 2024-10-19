<h1>Desafio: Manipulação e Tratamento de Arquivo CSV</h1>
<p>
  O objetivo deste desafio foi ler e manipular o arquivo <code>googleplaystore.csv</code> utilizando Python para análise de dados e geração de gráficos. 
  Todo o código, juntamente com suas respectivas saídas, pode ser encontrado no arquivo <strong>Desafio.ipynb</strong>, que exibe cada parte de forma estruturada.
</p>
<a href="/Sprint-3/Desafio/Desafio.ipynb">Acesse o arquivo ipynb</a> <br>

<h2>Passo a Passo para Resolução do Desafio</h2>
<p><strong>Ferramentas e bibliotecas utilizadas:</strong></p>
<ul>
  <li><strong>Jupyter Lab</strong></li>
  <li><strong>Pandas</strong></li>
  <li><strong>Matplotlib</strong></li>
</ul>

<ol>
  <h3>Leitura e Remoção de Duplicados do Arquivo CSV</h3>
  <li>
    Inicialmente, preparei o ambiente e importei o arquivo CSV para o Jupyter utilizando o Pandas, 
    com o comando <code>read_csv</code>, armazenando-o em uma variável chamada <strong>df</strong>.
  </li>
  <img src="/Sprint-3/Evidencias/configurando_ambiente.png" width="500px" alt="Configuração do Ambiente">

  <li>
    Para remover duplicatas, usei o comando <code>df.drop_duplicates()</code>, mas sem passar parâmetros inicialmente, 
    o que causou erros ao analisar os dados. Após orientação, entendi que era necessário remover duplicatas 
    com base no nome do App, ajustando para <code>df.drop_duplicates(subset='App', keep='first')</code>.
  </li>
  
  <strong>Exemplo de <code>drop_duplicates</code> sem parâmetros:</strong> <br>
  <img src="/Sprint-3/Evidencias/drop_duplicate_sem_parametro.png" width="500px" alt="Drop duplicates sem parâmetros"> <br>

  <strong>Exemplo de <code>drop_duplicates</code> com parâmetros:</strong> <br>
  <img src="/Sprint-3/Evidencias/drop_duplicate_com_parametro.png" width="500px" alt="Drop duplicates com parâmetros">
  
  <h3>Top 5 Apps Mais Instalados</h3>
  <li>
    Para encontrar os apps mais instalados, foi necessário tratar a coluna <code>Installs</code>, que continha dados não numéricos, 
    como <strong>","</strong>, <strong>"+"</strong> e <strong>"Free"</strong>. O tratamento foi feito sem alterar o arquivo original, 
    armazenando o resultado em uma variável tratada.
  </li>
  <li>
    Usei <code>.str.replace</code> para remover os caracteres indesejados e <code>.astype(float)</code> para converter os valores em numéricos. 
    A seleção dos 5 apps mais instalados foi feita com <code>df.nlargest(5, 'Installs')</code>.
  </li>
  <img src="/Sprint-3/Evidencias/top_5_apps.png" width="500px" alt="Top 5 apps mais instalados">

  <h3>Gráfico do Top 5 Apps Mais Instalados</h3>
  <li>
    Para criar o gráfico de barras, utilizei o <code>Matplotlib</code> com o comando <code>plt.bar</code>. 
    Adicionei labels com <code>plt.xlabel</code> e <code>plt.ylabel</code>, além do título com <code>plt.title</code>.
  </li>
  <li>
    Criei uma coluna de cores para personalizar as barras: <code>cores = ['blue', 'yellow', 'green', 'red', 'purple']</code>.
  </li>
  <li>
    Salvei o gráfico em PDF usando <code>plt.savefig('grafico_top5_apps_instalados.pdf', format='pdf', bbox_inches='tight')</code>.
  </li>
  <a href="/Sprint-3/Desafio/Graficos gerados/grafico_top5_apps_instalados.pdf">Baixar gráfico em PDF</a> <br>
  <strong>Exemplo de gráfico com ajuste de cores:</strong> <br>
  <img src="/Sprint-3/Evidencias/ajuste_cores_barra.png" width="500px" alt="Ajuste de cores no gráfico de barras"> <br>

  <h3>Categorias Presentes no Dataset</h3>
  <li>
    Utilizei o <code>groupby</code> na coluna <code>Category</code> para agrupar os apps por categoria, 
    contando o total de instalações. A visualização inicial não foi eficiente devido ao grande número de categorias. 
    Então, criei uma categoria "Outros" para apps com menos de 250 instalações, gerando um top 15 de categorias.
  </li>
  <li>
    Para criar o gráfico de pizza, usei <code>plt.figure</code> e <code>plt.pie</code>.
  </li>
  <img src="/Sprint-3/Evidencias/ajuste_grafico_pizza.png" width="500px" alt="Gráfico de pizza ajustado"> <br>
  <a href="/Sprint-3/Desafio/Graficos gerados/grafico_pizza_top_categorias.pdf">Baixar gráfico de pizza em PDF</a>

  <h3>App Mais Caro no Dataset</h3>
  <li>
    Para encontrar o app mais caro, tratei a coluna <code>Price</code> da mesma forma que fiz com <code>Installs</code>. 
    Utilizei o comando <code>precos_float.nlargest(1)</code> para identificar o valor mais alto e o <code>loc</code> para localizar o app correspondente.
  </li>
  <img src="/Sprint-3/Evidencias/app_mais_caro.png" width="450px" alt="App mais caro">

  <h3>Contagem de Apps com Classificação "Mature 17+"</h3>
  <li>
    Realizei a contagem dos apps com a classificação <code>"Mature 17+"</code> somando as ocorrências correspondentes.
  </li>
  <img src="/Sprint-3/Evidencias/mature17+.png" width="450px" alt="Contagem de apps Mature 17+">

  <h3>Top 10 Apps por Reviews</h3>
  <li>
    Separei as colunas <code>App</code> e <code>Reviews</code>, mas enfrentei erros porque alguns valores estavam sendo tratados como strings. 
    Para resolver, usei <code>pd.to_numeric</code> na coluna <code>Reviews</code> com o parâmetro <code>errors='coerce'</code>.
  </li>
  <img src="/Sprint-3/Evidencias/top_10_apps_reviews.png" width="450px" alt="Top 10 apps por reviews">

  <h3>Cálculos Realizados com o Dataset</h3>
  <ul>
    <li><strong>Média de Preço dos Apps por Categoria:</strong> Tratamento da coluna <code>Price</code> e uso da função <code>.mean()</code>.</li>
    <img src="/Sprint-3/Evidencias/media_preco_categoria.png" width="450px" alt="Média de preço dos apps por categoria">
    <li><strong>Total de Apps por Categoria:</strong> Soma dos apps por categoria.</li>
    <img src="/Sprint-3/Evidencias/quantidade_apps_categoria.png" width="450px" alt="Quantidade de apps por categoria">
    <li><strong>Média de Preço de Todos os Apps:</strong> Tratamento da coluna <code>Price</code> e cálculo da média.</li>
    <img src="/Sprint-3/Evidencias/media_preco_todos_apps.png" width="500px" alt="Média de preço de todos os apps">
    <li><strong>App Mais Barato do Dataset:</strong> Considerando apenas apps com preço maior que 0.</li>
    <img src="/Sprint-3/Evidencias/app_mais_barato.png" width="500px" alt="App mais barato">
  </ul>

  <h3>Gráfico de Dispersão e Gráfico de Linhas</h3>
  <strong>Gráfico de Dispersão:</strong>
  <ul>
    <li>Criei um gráfico de dispersão para analisar a relação entre o preço e o número de reviews, permitindo visualizar como as duas variáveis se comportam juntas.</li>
    <a href="/Sprint-3/Desafio/Graficos gerados/grafico_dispersao.pdf">Baixar gráfico de dispersão em PDF</a> <br>
    <img src="/Sprint-3/Evidencias/grafico_de_dispersao.png" width="500px" alt="Gráfico de dispersão">
  </ul>

  <strong>Gráfico de Linhas:</strong>
  <ul>
    <li>Criei um gráfico de linhas que mostra a evolução do número de apps lançados ao longo dos anos, evidenciando tendências no crescimento do mercado de aplicativos.</li>
    <a href="/Sprint-3/Desafio/Graficos gerados/grafico_linhas.pdf">Baixar gráfico de linhas em PDF</a> <br>
    <img src="/Sprint-3/Evidencias/grafico_de_linhas.png" width="500px" alt="Gráfico de linhas">
  </ul>

  <h3>Conclusão</h3>
  <p>
    Este desafio permitiu aplicar conceitos de manipulação de dados e visualização, além de aprofundar o conhecimento em Pandas e Matplotlib. 
    Os gráficos gerados ajudam a compreender melhor a distribuição e características dos aplicativos disponíveis na Play Store.
  </p>
</ol>
