SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where livro.publicacao > '2014-12-31'
order by cod;
