<h1>Visão Geral do Projeto por Sprint</h1>

<h2>Descrição Geral do Projeto</h2> 

<p>Este projeto foi desenvolvido em múltiplas sprints, com o objetivo de explorar, limpar, modelar e apresentar os dados de forma analítica e visual, utilizando ferramentas da AWS. O foco está em gerar insights acionáveis, com destaque para os gêneros de Comédia e Animação, a partir de um pipeline estruturado em camadas Raw, Trusted e Refined.</p>

<h2> Sprints do Projeto</h2>

Sprint 6: Exploração Inicial

<p>Esta etapa teve como objetivo explorar os arquivos .csv para compreender a estrutura e conteúdo dos dados. Não houve manipulação, apenas uma análise inicial para planejar os passos seguintes.</p> 
<ul> 
<li><strong>Atividade principal:</strong> Abrir os arquivos e explorar os dados disponíveis.</li>
<li><strong>Objetivo:</strong> Compreender a estrutura dos dados para planejar as próximas etapas.</li> 
</ul>

Sprint 7: Pesquisa e Contextualização

<p>Foram coletadas informações adicionais relevantes, com foco em complementar os dados existentes. Nenhuma manipulação foi realizada; apenas os dados necessários foram salvos em formato .json.</p> 
<ul> 
<li><strong>Atividade principal:</strong> Busca por dados adicionais relevantes.</li> 
<li><strong>Cuidados:</strong> Garantir que os dados sejam confiáveis, evitando fontes muito recentes ou inconsistentes.</li>
</ul>

Sprint 8: Limpeza e Padronização

<p>A etapa de limpeza padronizou as informações para eliminar inconsistências e preparar os dados para análise. Não houve transformação, apenas organização dos dados.</p> 
<ul> 
<li><strong>Atividade principal:</strong> Limpeza de dados irrelevantes e padronização dos formatos.
</li> <li><strong>Objetivo:</strong> Garantir consistência na base para as etapas seguintes.</li> </ul>

Sprint 9: Modelagem Dimensional

<p>Os dados das zonas Raw e Trusted foram tratados e unificados para criar um modelo dimensional Star Schema, preparado para a Camada Refined. O Apache Spark foi utilizado para transformações e o AWS Glue Data Catalog para a configuração de tabelas e views, possibilitando consultas no Amazon Athena e visualizações futuras no Amazon QuickSight.</p>
<ul> 
<li><strong>Atividades principais:</strong>
<ul> 
<li>Transformação e unificação de dados utilizando Apache Spark.</li>
<li>Modelagem multidimensional com foco nos gêneros Comédia e Animação.</li> 
<li>Configuração de tabelas no AWS Glue para consultas avançadas.</li> 
</ul>
</li> 
<li><strong>Objetivo:</strong> Preparar os dados para análises aprofundadas e Dashboards futuros.</li>
    </ul>
<h2> Sprint 10: Criação dos Dashboards</h2> 
<p>A etapa atual se concentra na visualização dos dados refinados. Dashboards estão sendo desenvolvidos no Amazon QuickSight, permitindo responder perguntas analíticas relacionadas à performance, retorno financeiro e popularidade, com destaque nos gêneros Comédia e Animação.</p>
 <ul> 
 <li><strong>Dashboards criados:</strong> 
 <ul> 
 <li><strong>Análise de Artistas e Popularidade:</strong> Respondendo perguntas sobre artistas, avaliações e gêneros.</li>
  <li><strong>Análise Temporal:</strong> Insights baseados em lançamentos ao longo dos anos.</li> 
  <li><strong>Análise Financeira:</strong> Foco no retorno financeiro e filmes com maiores receitas.</li> <li><strong>Análise de Performance:</strong> Combinação de todos os dashboards para insights abrangentes.</li> </ul> </li> 
  <li><strong>Ferramentas utilizadas:</strong> Amazon QuickSight, AWS Glue, Apache Spark, Amazon S3, Amazon Athena.</li>
   </ul>
<h2>Certificados</h2>
<p>Durante o projeto, a experiência prática foi o foco principal. Os conhecimentos adquiridos sobre AWS Glue, Amazon S3, modelagem dimensional e transformações com Apache Spark foram consolidados através do trabalho hands-on nas sprints anteriores. Esses aprendizados contribuíram significativamente para a execução bem-sucedida desta etapa do projeto.</p>
<h2>Comentários Finais</h2>
<p>O projeto foi uma jornada enriquecedora, que passou por todas as etapas de um pipeline de dados eficiente, culminando na criação de dashboards impactantes no Amazon QuickSight. Trabalhar com ferramentas da AWS como Glue, Athena e S3 proporcionou uma visão abrangente do processo de engenharia e análise de dados. A implementação do modelo dimensional e os insights extraídos destacaram-se como resultados-chave, sendo fundamentados em boas práticas de transformação e armazenamento de dados. Este esforço conjunto estabeleceu as bases para análises ainda mais avançadas no futuro.</p>
