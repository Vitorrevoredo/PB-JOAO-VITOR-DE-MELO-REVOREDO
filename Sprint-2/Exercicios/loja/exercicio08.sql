-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

SELECT 
	tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
LEFT JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd
GROUP BY tbvendas.cdvdd, tbvendedor.nmvdd
ORDER BY COUNT(tbvendas.cdven) DESC
LIMIT 1;