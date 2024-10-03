INSERT INTO "SELECT 
	 autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor 
LEFT JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado != ''PARANÁ''
GROUP BY autor.nome, editora.codeditora
ORDER BY autor.nome" (nome) VALUES
	 ('ABBASCHIAN,  R'),
	 ('ABE, Jair Minoro'),
	 ('ABREU, Antônio Suárez'),
	 ('ACEVEDO MARIN, Rosa Elizabeth'),
	 ('ALEXANDER, Charles K'),
	 ('ALLEN, P. A'),
	 ('ALMEIDA, Fernando José De'),
	 ('ALTMANN, Wolfgang'),
	 ('ALVARENGA, Beatriz Gonçalves De'),
	 ('ALVES, José Jerônimo De Alencar');
INSERT INTO "SELECT 
	 autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor 
LEFT JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado != ''PARANÁ''
GROUP BY autor.nome, editora.codeditora
ORDER BY autor.nome" (nome) VALUES
	 ('ALVES, William Pereira'),
	 ('AMADO, Nélia'),
	 ('AMALDI, U'),
	 ('AMARAL, Adriano Benayon Do'),
	 ('AMARAL, Luciano Do'),
	 ('ASTOLFI,  Jean-pierre'),
	 ('BARANENKOV, G. S'),
	 ('BARATA, Ronaldo'),
	 ('BARBALHO, Jader'),
	 ('BARBETTA, Pedro Alberto');
INSERT INTO "SELECT 
	 autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor 
LEFT JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado != ''PARANÁ''
GROUP BY autor.nome, editora.codeditora
ORDER BY autor.nome" (nome) VALUES
	 ('BARBOSA,  Ruy  Madsen'),
	 ('BARDÁLEZ  HOYOS,  Juan  L'),
	 ('BARISON, Thiago'),
	 ('BARP, Wilson José'),
	 ('BARROS, Regina Mambeli'),
	 ('BARSANO, Paulo Roberto');
