# leia a quantidade de notas
n = int(input("Digite o numero de notas: "))

# inicialize contador de notas
cont_rec = 0

# leia as notas e conte o numero de alunos de rec
i = 0 # contador de notas lidas
while i < n:
    nf = float(input("Digite uma nota: "))
    if 3 <= nf and nf < 5: #  equivalente a 3 <= nf < 5:
        cont_rec += 1
    i += 1

print(cont_rec, "alunos ficaram de recuperacao")
