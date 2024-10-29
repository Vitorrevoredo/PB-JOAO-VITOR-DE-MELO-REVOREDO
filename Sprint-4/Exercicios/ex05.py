def processar_notas(arquivo_csv):
    with open(arquivo_csv) as file:
        linhas = file.readlines() #abri e ler o arquivo csv
        resultados = []

        for dado in linhas:
            dados = dado.strip().split(',') #retira espaços vazios e separa com a virgula
            nome = dados[0] #nome
            notas = sorted(map(int, dados[1:]), reverse=True)[:3] # as 3 notas
            media = round(sum(notas) / 3, 2) #calcula a media
            resultados.append((nome, notas, media)) # adiciona na lista

    for nome, notas, media in sorted(resultados):
        print(f"Nome: {nome} Notas: [{notas[0]}, {notas[1]}, {notas[2]}] Média: {media}") #print da lista

# Chama a função com o arquivo 'estudantes.csv'
processar_notas('estudantes.csv')
