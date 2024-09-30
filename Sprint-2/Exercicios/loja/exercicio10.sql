-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
--  O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT 
    tbvendedor.nmvdd AS vendedor,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * (tbvendedor.perccomissao)/100,2) AS comissao
FROM tbvendas
JOIN tbvendedor ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.nmvdd
ORDER BY comissao DESC;