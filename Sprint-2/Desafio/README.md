# Desafio: Normalização da Tabela e Modelagens Dimensionais e Relacionais

O objetivo deste desafio era normalizar uma tabela de uma concessionária, aplicando as 3 Formas Normais (1FN, 2FN, 3FN) à sua estrutura, e, a partir disso, transformar o modelo relacional existente em um modelo dimensional. Isso permitiu a criação de consultas eficientes para análise de dados e relatórios.

## Problemas Encontrados e Soluções

- **Redundância de dados:** A tabela original tinha informações desorganizadas, o que aumentava o risco de erros e inconsistências. Isso foi resolvido pela criação de dimensões específicas.
- **Consultas ineficientes:** A falta de organização dificultava a execução de consultas complexas. Após a normalização e a criação do modelo dimensional, o desempenho das consultas foi melhorado.

## Passo a Passo para Resolução do Desafio

A abordagem que utilizei foi com o auxílio da ferramenta **DBeaver** para executar os comandos SQL e verificar o funcionamento da normalização. O desafio exigiu a separação de dados em tabelas distintas para eliminar redundâncias e melhorar a integridade dos dados. As Tabelas criadas foram:
- **Clientes**
- **Carros**
- **Vendedores**
- **Combustível**
- **Info_locacoes**

Essas dimensões permitiram a eliminação da duplicidade de dados e facilitaram a manutenção futura. O foco foi garantir que os dados fossem organizados de forma eficiente e atendessem às **Três Formas Normais**.

### Etapas Principais:

1. **Entendimento da Estrutura Original:** A tabela original de locações (`tb_locacao`) incluía informações redundantes sobre clientes, carros, vendedores e combustíveis. O primeiro passo foi identificar as entidades principais para criar um modelo relacional mais robusto.
   
2. **Normalização (1FN, 2FN, 3FN):** Dividi as informações em tabelas menores (dimensões), cada uma focada em uma entidade (Cliente, Carro, Vendedor, Combustível, Info_Locacoes). Isso eliminou a redundância de dados e melhorou a integridade. Coloquei cada id das tabelas como FOREIGN KEY na criação das tabelas, o que permitiu melhorar os relacionamentos e exemplificar as dependências no modelo relacional gerado.

3. **Evidências da Normalização e criação das relações:** Coloquei algumas imagens abaixo que mostram melhor os passos de criação das tabelas e ajuste das relações, inclusive com alguns erros encontrados durante o processo:

![Evidências da Normalização](SPRINT-2/Desafio/evidencias.png)

Para detalhar melhor os comandos SQL utilizados na normalização e criação das tabelas, fiz um arquivo de Formas Normais e um diretório com os scripts de criação das tabelas relacionais:

[Formas Normais e Normalização](SPRINT-2/Desafio/FormasNormais.sql)  
[Tabelas Relacionais Usadas](SPRINT-2/Desafio/tabelas-relacionais)

### Modelagem Dimensional
Na segunda etapa, converti o modelo relacional em um modelo dimensional. O modelo foi estruturado com a criação das views para cada dimensão: Cliente, Carro, Vendedor, Tempo e Combustível, e a tabela fato (`vw_fatos_locacao`) foi projetada para armazenar métricas essenciais, como quantidade de diárias e valor total. A maior dificuldade foi entender a criação das views e suas respectivas relações, mas após pesquisas e exemplos práticos, consegui criar um modelo dimensional eficiente.

---

## Consultas de Exemplos

Pensei em algumas perguntas que podem ser respondidas com minha tabela fato e dimensões:

1. **Qual é o valor total de locações por vendedor?**
   - Utiliza a **Dimensão Vendedor** e a **Tabela Fato** para calcular a soma dos valores das locações por vendedor.

2. **Quantas diárias foram feitas para cada cliente em determinado período?**
   - Usa a **Dimensão Cliente** e a **Dimensão Tempo** para agregar o total de diárias por cliente.

3. **Qual o carro mais alugado e qual seu tipo de combustível?**
   - Usa a **Dimensão Carro** e a **Dimensão Combustível** para identificar os carros mais alugados e seus respectivos tipos de combustível.

4. **Qual foi o valor total gerado pelas locações em um determinado período?**
   - Utiliza a **Dimensão Tempo** e a **Tabela Fato** para calcular o valor total das locações em um intervalo de tempo.

5. **Qual a média de valor de diárias por carro?**
   - Usa a **Dimensão Carro** e a **Tabela Fato** para calcular a média do valor das diárias por modelo de carro.

