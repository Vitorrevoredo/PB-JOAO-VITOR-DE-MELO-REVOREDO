<h1>Desafio: Manipulação e tratamento de arquivo csv</h1>
<p>
  O objetivo desse desafio era ler e manipular o arquivo <code>googleplaystore.csv</code> utilizando python para analise de dados e 
  geração de gráficos.
</p>
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
  <strong>- Drop_duplicate sem parametros</strong>
  
  <strong> - Drop_duplicate com parametros</strong>
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
<img src="/Sprint-2/Evidencias/grafico_de_barras.png" width=500px>
<h3>Categorias presentes no Dataset</h3>
<ul>
  <li>Para separar o apps por categoria utilizei o <code>groupby</code> na Category e contando por totais números de instalações</li>
  <li> Na primeira versão a vizualização das categorias não ficaram boas pois muitas foram encontradas, para resolver, coloquei uma 
  categoria de Outros que levava como parametro um limite de apps com menos de 250 instalações, que permitiu gerar o top 15 categorias.</li>
</ul>
<img src="/Sprint-3/Evidencias/erro_grafico_categorias.png" width=500px>
