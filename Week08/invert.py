seq = []

while True:

    n = int(input("Digite um número: "))    

    if n == 0: break

    seq.append(n)

# Percorre toda a lista em ordem inversa
for i in reversed(seq):

    print(i)
