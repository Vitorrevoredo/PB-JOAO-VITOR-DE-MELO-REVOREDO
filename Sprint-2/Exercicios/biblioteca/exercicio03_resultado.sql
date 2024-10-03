INSERT INTO "SELECT COUNT(LIVRO.cod) AS quantidade, 
       EDITORA.nome, 
       ENDERECO.estado, 
       ENDERECO.cidade
FROM LIVRO
JOIN EDITORA ON LIVRO.editora = EDITORA.codeditora
JOIN ENDERECO ON EDITORA.endereco = ENDERECO.codendereco
GROUP BY EDITORA.nome, ENDERECO.estado, ENDERECO.cidade
ORDER BY quantidade DESC
LIMIT 5
" (quantidade,nome,estado,cidade) VALUES
	 (138,' CBMM','PARANÁ','Guaratuba'),
	 (30,' Ática','SÃO PAULO','São Paulo');
