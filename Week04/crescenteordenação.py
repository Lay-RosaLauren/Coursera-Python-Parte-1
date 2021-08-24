print("Sequência numérica a ser digitada: 7, -6, 0, 12, 15, 37, 101, 201")

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
quarto = int(input('Quarto numero: '))
quinto  = int(input('Quinto numero : '))
sexto = int(input('Sexto numero: '))
sétimo = int(input('Sétimo numero: '))
oitavo  = int(input('Oitavo numero : '))

if primeiro < segundo < terceiro < quarto < quinto < sexto < sétimo < oitavo:
    print('crescente')

else:
    if not primeiro < segundo < terceiro < quarto < quinto < sexto < sétimo < oitavo:
        print('não está em ordem crescente')


