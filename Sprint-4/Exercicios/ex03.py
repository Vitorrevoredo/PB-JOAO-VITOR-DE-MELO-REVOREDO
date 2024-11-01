from functools import reduce
def calculo_do_saldo(lancamentos) -> float:
    calculador_do_valor= map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)  #separa valores de debito e credito
    resultado = reduce(lambda acc, val: acc + val, calculador_do_valor) # função reduce para calcular valores
    return resultado
    
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

resultado = calculo_do_saldo(lancamentos)
print(resultado)