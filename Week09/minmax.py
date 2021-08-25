def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', mínima(temperaturas), 'C.')
    print('A maior temperatura do mês foi: ', máxima(temperaturas), 'C.')

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def teste_pontual(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
        print('Valor errado para array', temp)
        print('Valor esperado: ', valor_esperado, 'Valor calculado: ', valor_calculado)
    
def testa_mínima():
    print('Iniciando os testes')
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([30, 27, 25, 26, 29, 30, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 22], 22)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print('Finalizando os testes')    
