'''Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, 
juntamente com seus valores correspondentes.
Como saída, imprima o ano em que a pessoa completará 100 anos de idade. '''

from datetime import date
nome = "Vitor"  
idade = 21      
anoAtual = int(date.today().strftime('%Y'))

nasc = anoAtual - idade
completou = nasc + 100

print(completou)

