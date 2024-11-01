def pares_ate(n:int):
    for i in range(2, n+1):
        if i % 2 ==0:
            yield i
print(list(pares_ate(10)))
# retorna valores pares, utilizando o passo =2 que garante os valores pares
# exemplo do uso do codigo com o numero 10, retornando uma lista dos valores pares
print(list(pares_ate(10)))
#resultado esperado:
[2, 4, 6, 8, 10]
