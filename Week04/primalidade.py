num = int(input("Digite um número inteiro: "))

if num < 2:
    print("não primo")
elif num == 2: 
    print("primo")
elif num % 2 == 0: 
    print("não primo")
else: 
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print("não primo")
            break 
    else:
        print("primo")
