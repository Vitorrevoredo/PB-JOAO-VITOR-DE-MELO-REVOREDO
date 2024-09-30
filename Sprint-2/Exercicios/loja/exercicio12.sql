-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). 
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT
    tbvendas.cdpro,
    tbvendas.nmcanalvendas,
    tbvendas.nmpro,
    SUM(tbvendas.qtd)*COUNT(cdpro) AS quantidade_vendas
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
    AND tbvendas.nmcanalvendas IN ('E-Commerce', 'Matriz')
GROUP BY tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
ORDER BY quantidade_vendas ASC
