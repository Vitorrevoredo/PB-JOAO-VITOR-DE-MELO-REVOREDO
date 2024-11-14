<h1>Análise do Conjunto de Dados de Vendas de Títulos do Tesouro Direto e Utilização do Serviço S3 da AWS</h1>

<h2>Descrição do Projeto</h2>
<p>Esta sprint teve como objetivo analisar um conjunto de dados usando Python, utilizei as bibliotecas boto3, pandas e io para estabelecer conexão, limpeza e manipulação de dados. Além disso, integrei o projeto com o serviço de armazenamento S3 da AWS, configurando e manipulando buckets e arquivos via AWS CLI e Python. As etapas incluíram desde a configuração de permissões até a análise detalhada dos dados.</p>

<h2>Passo a Passo para Resolução do Desafio</h2>
<ol>
  <li><strong>Criação do Usuário IAM e Configuração do AWS CLI</strong></li>
  <p>Para estabelecer a conexão com o bucket do S3, instalei o <strong>AWS CLI</strong>, que permite interagir com os serviços da AWS diretamente pelo terminal, sem precisar acessar o Console de Gerenciamento. Fui instruído a criar um usuário IAM, necessário para gerar as Credenciais de Acesso (Access Key ID: identificador único da chave de acesso e Secret Access Key: chave secreta associada ao Access Key ID), essenciais para gerenciar os recursos da AWS. Com isso, iniciei a criação do meu usuário.</p>
  <img src="/Sprint-5/Evidencias/criando_user_iam.png" width="500px" alt="Nenhum usuário criado"> <br>
  <img src="/Sprint-5/Evidencias/criando_usuario_iam.png" width="500px" alt="Usuário IAM criado"> <br>
 <p>Após criar o usuário, criei um grupo de usuários para aplicar as permissões de acesso necessárias. Além disso, ativei o <strong>MFA</strong> (autenticação multifatorial) para aumentar a segurança da conta. Durante a criação do grupo, concedi a permissão <code>AmazonS3FullAccess</code> para garantir acesso total ao S3. Em seguida, adicionei meu usuário ao grupo e configurei as credenciais de acesso no terminal para estabelecer a conexão com a AWS.</p>
   <p>Com as configurações feitas, realizei alguns testes de conexão utilizando os comandos <code>aws s3 ls</code> e <code>aws sts get-caller-identity</code>, que devem listar os buckets criados e testar a conexão, respectivamente. Durante os testes, encontrei erros de permissão relacionados às Políticas de Controle de Serviços (SCPs), que afetam a capacidade de gerenciar usuários. Pesquisando mais sobre o assunto, descobri que as SCPs são aplicadas no nível da conta ou unidade organizacional e possuem uma política de negação implícita. Como não era possível aplicar as permissões, o time técnico da Compass sugeriu o uso de chaves temporárias para realizar as operações necessárias. Refiz o processo de configuração aplicando as chaves de acesso já fornecidas na minha conta aws.</p>
  <img src="/Sprint-5/Evidencias/erro_aws_conexao.png" width="500px" alt="Erros nas permissões AWS"> <br>
  <img src="/Sprint-5/Evidencias/conexao_chaves_temp.png" width="500px" alt="Conexão estabelecida"> <br>
  <img src="/Sprint-5/Evidencias/acesso_s3.png" width="400px" alt="Acesso ao S3 para meu usuário"> <br>
  <img src="/Sprint-5/Evidencias/chaves_de_acesso.png" width="500px" alt="Chaves de acesso padrão"> <br>


  <li><strong>Bucket s3 </strong></li>
  <p>Para armazenar o arquivo de dados no S3, criei um bucket usando a interface AWS. Nomeei o bucket como <strong>bucket-desafio-vitor</strong>, pois cada bucket requer um nome único. As permissões foram configuradas para garantir upload e leitura dos arquivos. Ao finalizar o Desafio exclui o bucket.</p>
  <img src="/Sprint-5/Evidencias/criando_bucket_s3.png" width="500px" alt="Bucket s3"> <br>
  <img src="/Sprint-5/Evidencias/excluindo_bucket.png" width="500px" alt="Excluindo bucket aws"> <br>


  <li><strong>Escolha e Estrutura do Conjunto de Dados</strong></li>
  <p>Escolhi um conjunto de dados do site indicado, contendo informações sobre vendas de títulos do Tesouro Direto ao longo dos últimos anos. O conjunto incluía colunas como:</p>
  <ul>
    <li><strong>Tipo Título</strong>: Tipo de título (Tesouro Prefixado, Tesouro Selic, Tesouro IGPM+ com Juros Semestrais).</li>
    <li><strong>Vencimento do Título</strong>: Data de vencimento do título.</li>
    <li><strong>Data Venda</strong>: Data da venda do título.</li>
    <li><strong>PU</strong>: Preço Unitário do título na venda.</li>
    <li><strong>Quantidade</strong>: Quantidade de títulos vendidos.</li>
    <li><strong>Valor</strong>: Valor total da venda.</li>
  </ul>

  <li><strong>Implementação do Script de Upload em Python para Conexão com o S3</strong></li>
  <p>Após a configuração do ambiente, desenvolvi um script Python usando a biblioteca <strong>boto3</strong>, que permite interagir com o S3. O script define as configurações do cliente S3 e faz o upload do arquivo <code>VendasTesouroDireto.csv</code> do diretório local para o bucket S3 configurado. Adicionei comentários explicando cada etapa do código.</p>
  <a href="/Sprint-5/Desafio/s3_upload_script.py">Acesse o arquivo de upload</a> <br>
  <img src="/Sprint-5/Evidencias/envio_arquivo.png" width="500px" alt="Envio arquivo para o bucket"> <br>
  <img src="/Sprint-5/Evidencias/teste_upload_arquivo_concluido.png" width="500px" alt="Envio arquivo para o bucket"> <br>


  <li><strong>Script de Manipulação de Arquivo CSV</strong></li>
  <p>Para manipular o arquivo CSV e realizar pesquisas, desenvolvi um script Python que realiza as seguintes ações:</p>
  <ul>
    <li><strong>Limpeza de Dados</strong>: Converti valores de <code>PU</code>, <code>Quantidade</code> e <code>Valor</code> para <strong>float</strong> e substituí vírgulas por pontos.</li>
    <li><strong>Filtragem de Dados</strong>: Apliquei filtros para selecionar apenas vendas onde <code>PU > 1000</code> e <code>Quantidade < 50</code>, visando identificar vendas mais específicas.</li>
    <li><strong>Cálculos de Média e Soma</strong>: Calculei a média do <strong>PU</strong> e a soma do <strong>Valor</strong> das vendas, obtendo insights sobre preços e volumes totais das transações.</li>
    <li><strong>Categorização de Valores</strong>: Classifiquei as vendas como "Alto" ou "Baixo" de acordo com o <code>Valor</code> total, facilitando a análise das vendas por faixa de valor.</li>
    <li><strong>Conversão de Datas</strong>: Converti a coluna <code>Data Venda</code> para o formato <strong>datetime</strong>, permitindo análises temporais e extração do ano da venda.</li>
    <li><strong>Normalização de Textos</strong>: Padronizei os valores de <code>Tipo Título</code> para maiúsculas, garantindo consistência na categorização dos títulos.</li>
  </ul>
   <a href="/Sprint-5/Desafio/processamento_pandas.py">Acesse o arquivo de tratamento de dados</a> <br>
   <img src="/Sprint-5/Evidencias/upload_arquivo_modificado.png" width="500px" alt="Envio arquivo para o bucket"> <br>

   <li>Erros exemplos na manipulação dos dados que encontrei</li>
  <img src="/Sprint-5/Evidencias/erro_tratamento_dados.png" width="500px" alt="Erros manipulação 1"> <br>
  <img src="/Sprint-5/Evidencias/erro_tratamento_dados2.png" width="500px" alt="Erros manipulação 2"> <br>
  <img src="/Sprint-5/Evidencias/resolvendo_erro_tratamento_dados.png" width="500px" alt="Erros resolvido"> <br>
</ol>

<h2>Resultados</h2>
<ul>
  <li><strong>Vendas Filtradas</strong>: Os dados filtrados incluem apenas vendas com <strong>PU > 1000</strong> e <strong>Quantidade < 50</strong>, oferecendo um conjunto específico de transações para análise detalhada.</li>
  <li><strong>Média do PU</strong>: A média do <strong>PU</strong> foi calculada como <strong>(valor calculado)</strong>, representando o preço médio unitário das vendas.</li>
  <li><strong>Soma do Valor</strong>: A soma total das vendas foi <strong>(valor calculado)</strong>, destacando o volume financeiro das transações.</li>
  <li><strong>Categorização de Vendas</strong>: Cada venda foi classificada como "Alto" ou "Baixo", com base no <code>Valor</code>, possibilitando a identificação de vendas de alto valor.</li>
  <li><strong>Análise Temporal</strong>: A extração do ano permitiu identificar tendências e comportamentos nas vendas ao longo dos anos.</li>
  <li><strong>Padronização de Títulos</strong>: Os valores de <code>Tipo Título</code> foram uniformizados em maiúsculas para evitar inconsistências nas análises.</li>
</ul>

<h2>Conclusão</h2>
<p>Com a análise dos dados de vendas de títulos do Tesouro Direto, foi possível identificar informações relevantes sobre preços e volumes de vendas, como vendas de alto valor e padrões anuais. A integração com o AWS S3 demonstrou-se eficiente para armazenamento e manipulação de grandes volumes de dados. O uso de ferramentas como o <strong>AWS CLI</strong>, <strong>boto3</strong> e <strong>Pandas</strong> facilitou o acesso, a limpeza e a análise dos dados. As etapas de filtro, conversão e agregação permitiram transformar o conjunto bruto em dados mais organizados e informativos para análises futuras.</p>
