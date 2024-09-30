--Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.


SELECT 
	tbvendas.cdven
FROM tbvendas
WHERE tbvendas.deletado = 1
GROUP BY cdven
ORDER BY cdven 