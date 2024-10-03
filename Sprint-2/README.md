# README - Projeto de Modelagem de Banco de Dados

<h2>Instruções</h2>

<p>Este projeto tem como objetivo aplicar técnicas de normalização e modelagem dimensional em um banco de dados de uma concessionária.</p>

1. Utilizar ferramentas como **DBeaver** ou **SQLite** para executar os scripts SQL.
2. Normalizar a tabela de locações aplicando as **Três Formas Normais (1FN, 2FN, 3FN)**.
3. Após a normalização, transformar o modelo relacional em um **modelo dimensional**.

<h2>Objetivos da Sprint</h2>

<ul>
  <li> Praticar a linguagem SQL por meio de Exercicios propostos</li>
  <li>Aplicar as 3 Formas Normais na tabela original de locações para melhorar a integridade e consistência dos dados.</li>
  <li>Criar tabelas relacionais organizadas para eliminar redundâncias e melhorar a eficiência.</li>
  <li>Converter o modelo relacional para o dimensional e criar views para consultas rápidas e eficientes.</li>
  <li>Responder a perguntas relacionadas ao desempenho das locações com base nas dimensões e na tabela fato.</li>
</ul>

<h2>Informações</h2>

<ul>
  <li>Ferramentas utilizadas: <strong>DBeaver</strong>, <strong>SQLite</strong>, <strong>SQL</strong>.</li>
  <li>Tabelas principais:
    <ul>
      <li><strong>Clientes</strong></li>
      <li><strong>Carros</strong></li>
      <li><strong>Vendedores</strong></li>
      <li><strong>Combustível</strong></li>
      <li><strong>Info_locacoes</strong> (Tabela Fato)</li>
    </ul>
  </li>
</ul>

<h2>Anotações</h2>

<p>Peguei como base os cursos da Udemy e busquei aprofundar o conhecimento através de outros métodos, como fóruns especializados e vídeos no YouTube, que forneceram exemplos práticos e diferentes abordagens para resolver os problemas encontrados.</p>

<p>Durante o processo de desenvolvimento, fiz algumas observações importantes:</p>

<ul>
  <li><strong>Redundância de dados:</strong> Ao longo da modelagem, percebi a presença de redundâncias, que foram eliminadas aplicando as Formas Normais. Isso ajudou a organizar melhor as tabelas e reduzir a duplicação de informações.</li>
  <li><strong>Otimização de consultas:</strong> A criação de tabelas de dimensões e a tabela fato ajudaram a consolidar os dados, permitindo consultas mais rápidas e eficientes, o que melhorou significativamente a performance do sistema.</li>
  <li><strong>Chaves estrangeiras (FOREIGN KEYS):</strong> A definição de chaves estrangeiras entre as tabelas foi fundamental para garantir a integridade referencial e evitar inconsistências nos dados relacionados.</li>
  <li><strong>Integração de novos dados:</strong> A estrutura projetada também permite a inclusão de novos dados sem a necessidade de grandes alterações no banco, mantendo a flexibilidade e escalabilidade.</li>
</ul>

<h2>Exercícios</h2>

<p>Para resolução dos exercicios utilizei o DBeaver como base para ir testando as querys de pesquisa e obter os resultados solicitados em cada exercicio, e realizando os ajustes até obter os resultados corretos!</p>

<img src="/Sprint-2/Exercicios/evidencias/exemplo_ex.png" width="450px">
<img src="/Sprint-2/Exercicios/evidencias/erro_biblioex04.png" width="500px">
<img src="/Sprint-2/Exercicios/evidencias/evidencia_conclusão_exe.png" width="400px">

<strong>Evidencia de conclusão de Todos exercicios</strong>
<p>Coloquei como anexo o geral de evidencia de conclusão de todos , para evitar redundancia de colocar cada aba!</p>
<img src="/Sprint-2/Exercicios/evidencias/loja_evidencia.png" width="350px">
<img src="/Sprint-2/Exercicios/evidencias/biblioteca_evidencia.png" width="350px">


<h2>Exercicios resolvidos</h2>
<p>Fiz uma pasta para cada exercicio que coloquei o codigo das querys utilizadas e resultados obtidos em cada exercicio</p>
<li><a href="/Sprint-2/Exercicios/biblioteca/">Exercicios Biblioteca</a></li>
<li><a href="/Sprint-2/Exercicios/loja/">Exercicios Loja</a></li>
<li><a href="/Sprint-2/Exercicios/exportação-de-dados/">Exercicios Exportação de Dados</a></li>

<h2>Certificados</h2>
<p>Fiz o Curso da Udemy da trilha que informaram que não era necessario anexar e também optei por fazer outros na propria plataforma que utilizei para estudar, anexo do curso que fiz por fora e da Aws: </p>
<img src="/Sprint-2/Exercicios/evidencias/Banco de Dados do Zero ao Avançado.jpg" width="400px">
<li><a href="/Sprint-2/Certificados/Aws partner accreditation (business).pdf">Certificado Aws</a></li>

<h2>Comentários Finais</h2>

<p>O desafio foi resolvido com sucesso, resultando em uma estrutura de dados organizada e eficiente para futuras análises e consultas. A aplicação das 3 Formas Normais, seguida pela criação de um modelo dimensional, não apenas melhorou a clareza e a performance do banco de dados, mas também garantiu a integridade dos dados e facilitou a execução de consultas complexas.</p>

<p>A normalização e modelagem de dados foram etapas desafiadoras, mas extremamente enriquecedoras. O processo de eliminação de redundâncias, criação de dimensões e estruturação da tabela fato proporcionou um entendimento mais profundo sobre a importância de uma base de dados bem projetada. Esse aprendizado será fundamental para enfrentar desafios mais complexos em futuros projetos de análise e modelagem de dados.</p>

