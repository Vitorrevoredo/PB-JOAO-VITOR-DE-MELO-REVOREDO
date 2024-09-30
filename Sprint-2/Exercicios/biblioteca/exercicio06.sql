-- Apresente a query para listar o autor com maior número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes

SELECT
	autor.codautor,
	autor.nome,
	COUNT(livro.cod) as quantidade_publicacoes
from livro
LEFT JOIN autor ON livro.autor = autor.codautor
GROUP BY autor.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1