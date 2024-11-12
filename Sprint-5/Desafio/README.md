# Análise do Conjunto de Dados de Vendas de Títulos do Tesouro Direto

Este conjunto de dados contém informações sobre as vendas de diferentes tipos de títulos do Tesouro Direto.

### Estrutura do Conjunto de Dados

- **Tipo Titulo**: Tipo de título (Tesouro Prefixado, Tesouro Selic, Tesouro IGPM+ com Juros Semestrais).
- **Vencimento do Titulo**: Data de vencimento do título.
- **Data Venda**: Data da venda do título.
- **PU**: Preço Unitário do título na venda.
- **Quantidade**: Quantidade de títulos vendidos.
- **Valor**: Valor total da venda.

### Consultas e Manipulações Realizadas

1. **Filtragem de Dados**: Filtrei os dados onde o PU é maior que 1000 e a Quantidade é menor que 50.
2. **Funções de Agregação**:
   - Média do PU:
   - Soma do Valor: 
3. **Função Condicional**: Classificação de vendas em "Alto" ou "Baixo" com base no valor da venda.
4. **Função de Conversão**: Conversão da coluna "Data Venda" para o formato datetime.
5. **Função de Data**: Extração do ano da data da venda para análise.
6. **Função de String**: Conversão dos valores da coluna "Tipo Titulo" para maiúsculas.

### Resultados


