INSERT INTO "SELECT
	autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
GROUP BY autor.nome
ORDER BY livro.cod
LIMIT 8" (nome) VALUES
	 ('ABUNAHMAN, Sérgio Antonio'),
	 ('ALLINGER, Norman L (et al)'),
	 ('ALMEIDA, Alfredo Wagner Berno De'),
	 ('ALMEIDA, Salvador Luiz De'),
	 ('BABBITT, Harold E'),
	 ('BALBO, José Tadeu'),
	 ('BARBOSA, Estêvão José Da Silva'),
	 ('BARROS, Maria Vitória Martins');
