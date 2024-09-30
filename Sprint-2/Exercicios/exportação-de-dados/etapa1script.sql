-- Seção 6
SELECT
	livro.cod,
	livro.titulo,
	autor.codautor,
	autor.nome,
	livro.valor,
	editora.codeditora,
	editora.nome
from livro
JOIN autor ON livro.autor = autor.codautor
JOIN editora ON livro.editora = editora.codeditora
GROUP BY livro.cod, livro.titulo, livro.valor
order by valor desc
limit 10;