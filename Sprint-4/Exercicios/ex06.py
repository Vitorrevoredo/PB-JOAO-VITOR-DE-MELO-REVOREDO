def maiores_que_media(conteudo:dict)->list:
     # Calcula a média dos preços
    media = sum(conteudo.values()) / len(conteudo)

    # Filtra os produtos acima da média e cria uma lista de tuplas
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    produtos_ordenados = sorted(produtos_acima_media, key=lambda x: x[1])

    return produtos_ordenados