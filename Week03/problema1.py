n = int(input("Digite o tam da seq: "))
contap = 0
contai = 0
i = 1
while i <= n:
    num = int(input("Digite um num da seq: "))
    if num%2 == 0: #par
        contap = contap + 1
    else: #ímpar
        contai = contai + 1
    i = i + 1
print(contap,"números pares")
print(contai,"números ímpares")
