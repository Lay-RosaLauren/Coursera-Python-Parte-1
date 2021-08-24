tamanho = int(input("Digite o tamanho da sequência de números: "))
print("Digite uma sequência de valores terminada por zero.")

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite o valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("O produto dos valores digitados é: ", produto)    
