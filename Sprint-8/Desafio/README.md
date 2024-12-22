Como decidi focar minha analise em Filmes dos meus generos (Comédia e Animação) 
Para limpeza dos dados e deixar mais confiavel na minha camada Trusted no csv usei os seguintes criterios
Limpezas que melhorem a confiabilidade dos dados, como:

Verificar e remover linhas com campos incompletos ou inconsistentes:

Linhas com valores nulos (\N ou vazios).
Campos importantes, como id, tituloPincipal, e anoLancamento, precisam ser obrigatórios.
Validação e padronização de campos específicos:

Confirmar que anoLancamento tem apenas números válidos.
Garantir que genero seja categorizado corretamente.
Filtrar e ajustar dados sobre pessoas e personagens:

Verificar se campos como anoNascimento ou anoFalecimento fazem sentido e padronizar o formato, removendo valores inválidos (\N).


Limpeza Básica dos Dados JSON:

Exclusão de Linhas Nulas: Removemos qualquer linha onde tmdb_id, title, ou release_date estão ausentes.
Ano de Lançamento: Garantimos que o ano seja maior que 1888.
Validação de Gênero e Campos Relevantes: O código filtra filmes que têm o campo genres nulo, o que ajuda a garantir qualidade de dados. Além disso, valida o número de votos e a média de notas.
Filtragem de Filmes de Coleção: Agora também está sendo realizada uma verificação para garantir que o campo belongs_to_collection esteja presente para os filmes da franquia.