-- Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

SELECT a.codautor, 
       a.nome, 
       a.nascimento, 
       COUNT(l.cod) AS quantidade
FROM autor a
LEFT JOIN LIVRO l ON l.autor = a.codautor
GROUP BY a.codautor, a.nome, a.nascimento
ORDER BY a.nome ASC;
