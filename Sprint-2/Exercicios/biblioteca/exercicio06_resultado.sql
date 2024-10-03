INSERT INTO "SELECT
	autor.codautor,
	autor.nome,
	COUNT(livro.cod) as quantidade_publicacoes
from livro
LEFT JOIN autor ON livro.autor = autor.codautor
GROUP BY autor.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1" (codautor,nome,quantidade_publicacoes) VALUES
	 (67,'BARP, Wilson José',7);
