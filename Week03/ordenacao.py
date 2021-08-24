primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

if primeiro < segundo < terceiro:
    print('crescente')

else:
    if not primeiro < segundo < terceiro:
        print('não está em ordem crescente')


