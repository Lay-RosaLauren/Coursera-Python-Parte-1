print("Calcular as raízes de uma equação do segundo grau:")

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    X = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", X)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        X = (-b + math.sqrt(delta)) / (2 * a)
        Y = (-b - math.sqrt(delta)) / (2 * a)
        result = X,Y
        print("as raízes da equação são",sorted(result))
   
