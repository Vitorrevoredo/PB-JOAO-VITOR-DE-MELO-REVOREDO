-- ETAPA 2
SELECT 
	editora.codeditora,
    editora.nome,
    COUNT(livro.cod) AS quantidade
FROM livro
LEFT JOIN editora ON livro.editora = editora.codeditora
GROUP BY editora.nome, editora.codeditora
ORDER BY quantidade DESC
LIMIT 5;