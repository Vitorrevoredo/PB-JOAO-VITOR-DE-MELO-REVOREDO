with open('number.txt') as arquivo:
    linhas = arquivo.readlines()

linhas = list(map(int, linhas)) #transformação de dados
pares= list(filter(lambda x: x%2 ==0, linhas)) # filtro de numeros pares
maiores_pares= sorted(pares, reverse= True)[:5] # ordenação e top numeros pares
soma_maiores_pares= sum(maiores_pares) #soma os maiores valores pares

print(maiores_pares)
print(soma_maiores_pares)
### Resposta
[8000, 7998, 7996, 7994, 7994]
39982