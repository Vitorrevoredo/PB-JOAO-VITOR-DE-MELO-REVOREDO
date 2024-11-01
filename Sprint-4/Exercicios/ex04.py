def calculo_valor_maximo(operadores, operandos):
    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else 0,  # Retorna 0 no caso de divisão por zero
        '%': lambda a, b: a % b
    }
    
    # Aplicar as operações sobre os operandos
    resultado_calculo = map(lambda op: operacoes[op[0]](op[1][0], op[1][1]), zip(operadores, operandos))
    
    # Retornar o maior valor
    return max(resultado_calculo)

operadores = ['+', '-', '*', '/', '+']
operandos  = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
resultado = calculo_valor_maximo(operadores, operandos)
print(resultado)
