def conta_vogais(texto:str)-> int:
    vogais= "aeiou" #vogais
    return len(list(filter(lambda x: x in vogais, texto.lower()))) #retorno da quantidade de  vogais presentes na palavra/texto
resultado = conta_vogais("Ola mundo, este e um importante teste")
print(resultado)
## Resultado
14
