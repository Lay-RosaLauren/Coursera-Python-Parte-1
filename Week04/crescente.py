n = int(input("Digite o tam da seq: "))
ant = int(input("Digite um num da seq: "))
cresce = True
i = 2
while i <= n and cresce:
    num = int(input("Digite um num da seq: "))
    if num <= ant:
        cresce = False
    ant = num
    i = i + 1
 
if cresce:
    print("Sequência crescente")
else:
    print("Sequência não é crescente")
