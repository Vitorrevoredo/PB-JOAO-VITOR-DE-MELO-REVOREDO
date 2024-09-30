--Apresente a query para listar o nome dos autores com nenhuma publicação. 
-- Apresentá-los em ordem crescente.

SELECT
	autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
GROUP BY autor.nome
ORDER BY livro.cod
LIMIT 8;
