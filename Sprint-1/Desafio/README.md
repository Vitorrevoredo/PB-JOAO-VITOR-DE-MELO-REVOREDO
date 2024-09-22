# Desafio: Automação de Backups e Geração de Relatórios Diários

<h1>Este desafio teve como objetivo automatizar o processo de geração de backups de vendas, criando relatórios diários com base nos dados fornecidos em um arquivo `.csv` e, por fim, consolidar todos os relatórios em um arquivo final.</h1>

## Passo a Passo para Resolução do Desafio

<h2>A abordagem utilizada foi resolver os passos diretamente no terminal para entender como os comandos funcionariam e como seria possível automatizá-los via script `.sh`. Após testar e entender os processos, passei a organizar o código no script principal.</h2>

### 1. Estruturação de Pastas

<p>1.1 Estruturei as pastas para o desafio com base no modelo solicitado:</p>
<img src="/Sprint-1/Evidencias/exemplo_pastas.png" alt="Estrutura de Pastas" width="400px">

### 2. Desenvolvimento do Script

<p>2.1 Criação do arquivo executável `.sh`, que serve como o script principal do projeto:</p>
<img src="/Sprint-1/Evidencias/Evidencia_de_arquivo_sh_executavel.png" alt="Arquivo sh Executável" width="400px" height="300px">

2.2 Métodos Utilizados

<p>Decidi utilizar variáveis para armazenar a data do sistema, além de calcular a primeira e última venda no arquivo de dados. A variável de data foi definida rapidamente, mas as variáveis de primeira e última venda exigiram mais ajustes ao longo do projeto. Testei diferentes abordagens usando comandos como `awk`, `cut`, `head`, `tail` e `sort` para otimizar o código.</p>

<ul>
  <li><strong>data_sistema</strong>: Armazena a data atual do sistema.</li>
  <li><strong>quantidade_produtos, primeira_data e ultima_data</strong>: Contam os itens vendidos e registram a primeira e a última data de venda, respectivamente. Embora a primeira data não tenha sido modificada no arquivo, criei essa variável para evitar possíveis erros futuros.</li>
</ul>

<img src="/Sprint-1/Evidencias/variaveis.png" alt="Configuração das Variáveis" width="600px">
<img src="/Sprint-1/Evidencias/resultado config sort 01.png" alt="Resultado teste de execução" width="400px">
<img src="/Sprint-1/Evidencias/configurandosort.png" alt="Configuração do Sort" width="600px">
<img src="/Sprint-1/Evidencias/uso do awk.png" alt="Uso do awk" width="600px">
<img src="/Sprint-1/Evidencias/datacorreta.png" alt="Data correta" width="500px">
2.3 Solução para Caminhos de Arquivos

<p>Percebi a importância de usar caminhos absolutos para garantir que o script funcionasse corretamente. Embora pudesse ter utilizado variáveis para armazenar os caminhos, optei por deixá-los explícitos no código. Isso foi uma excelente prática para aprimorar meu entendimento do Linux.</p>

<img src="/Sprint-1/Evidencias/acessodiretorios.png" alt="Acesso aos Diretórios" width="600px">

2.4 Criação do Relatório

<p>Para gerar o relatório e inserir as informações, utilizei o comando `echo`, que me permitiu definir a estrutura e o conteúdo do relatório de forma clara. Exemplo:</p>
echo "Data do Sistema: $(date +"%Y/%m/%d %H:%M")" >> relatorio.txt-${data_sistema}

<p>Essa abordagem permitiu uma organização mais legível e apresentável no relatório final.</p>
Para adicionar as 10 primeiras linhas do arquivo de backup, usei o comando head, passando as 11 primeiras linhas e redirecionando-as para o arquivo de relatório com o operador >>.
<img src="/Sprint-1/Evidencias/echouso.png" alt="Uso do Echo no Relatório" width="600px">
2.5 Compactação e Remoção de Arquivos
<p>Para criar o arquivo compactado (ZIP), usei o comando `zip` com a data do sistema no nome do arquivo. Em seguida, o comando `rm` foi utilizado para apagar os arquivos CSV desnecessários, mantendo apenas o backup compactado.</p> 
<img src="/Sprint-1/Evidencias/removearquivos.png" alt="Remoção arquivos" width="600px">
<img src="/Sprint-1/Evidencias/arquivozip.png" alt="Criação do Arquivo ZIP" width="600px">
<img src="/Sprint-1/Evidencias/arquivo zip gerado.png" alt="Evidencia de arquivo ZIP" width="600px">
<h3>3. Evidências do Código</h3>
<p>Abaixo estão algumas das versões do código que utilizei durante o processo, além das evidências visuais que ajudam a ilustrar cada , sendo a ultima imagem a versão final do codigo.</p>
<img src="/Sprint-1/Evidencias/primeira_versao_executavel.png" alt="Primeira versao do codigo" width="400px">
<img src="/Sprint-1/Evidencias/teste1.png" alt="Teste execucao 1" width="400px">
<img src="/Sprint-1/Evidencias/versao01.png" alt ="Versao 1 do codigo" width="400px">
<img src='/Sprint-1/Evidencias/versao02.png' alt="Versao 2 do codigo" width="400px">
<img src="/Sprint-1/Evidencias/versao03.png" alt="Versão 3 do codigo" width="400px">
<img src="/Sprint-1/Evidencias/versaoutilizada.png" alt="Versao utilizada" width="600px">
<h3>4. Crontab</h3>
<p>
Para automatizar a execução do arquivo durante os 4 dias e a geração dos relatórios, resolvi usar o `crontab`, facilitando o processo de automatização. Fiz um teste antes de agendar da forma correta, e depois coloquei o arquivo de evidencia de teste.
</p>
<img src="/Sprint-1/Evidencias/configurando crontab teste 01.png" alt="Teste crontab 1" width="400px"> 
<img src="/Sprint-1/Evidencias/resultado config sort 01.png" alt="Resultado teste de execução" width="400px">
<img src="/Sprint-1/Evidencias/crontab final.png" alt="Versao do crontab utilizada" width="600px">
<h3>5. Relatorio final:</h3>
Para consolidar o processamento após os 4 dias, criei um segundo script `.sh` como solicitado. Esse script usa o comando `cat` para combinar todos os arquivos `.txt` e gerar um relatório , coloquei como evidencia o resultado do teste.
<img src="/Sprint-1/Evidencias/consolidador_versao1.png" alt="Versão 1 do consolidador" width="600px">
<img src="/Sprint-1/Evidencias/testeconsolidador.png" alt="Teste consolidador" width="400px">
<img src="/Sprint-1/Evidencias/resultadoconsolidador.png" alt="Resultado teste consolidador" width="400px">
<h3>6. Comentários Finais</h3>
<p>O desafio foi resolvido com sucesso utilizando scripts em Bash que realizam o processamento e backup dos arquivos de vendas, geram relatórios diários e consolidam os resultados em um relatório final de 4 dias. A estrutura foi organizada de forma a permitir a execução diária sem perda de dados, garantindo que os relatórios sejam gerados com base nos dados corretos.</p>
<p>
 <strong>Todos os relatórios são gerados de forma incremental, portanto, a execução diária dos scripts irá garantir que os arquivos não sejam sobrescritos, e novos backups e relatórios sejam criados automaticamente.</strong>
</p>
