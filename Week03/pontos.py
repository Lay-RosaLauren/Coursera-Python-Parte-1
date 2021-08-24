print("Distância entre dois pontos em um plano cartesiano")
import math
# Inserido coordenadas dos pontos
x1 = float(input("Digite um número correspondente a x1: "))
y1 = float(input("Digite um número correspondente a y1: "))

x2 = float(input("Digite um número correspondente a x2: "))
y2 = float(input("Digite um número correspondente a y2: "))

if x1 < 0 and y1 >= 0:  
    xy1 = (x1*-1) + y1
elif x1 >= 0 and y1 < 0:
    xy1 = x1 + (y1 * -1)
elif x1 < 0 and y1 < 0:
    if x1 > y2:
        xy1 = x1 - y1
    else:
        xy1 = y1 - x1
elif x1 >= 0 and y1 >= 0:
    if x1 >= y1:
        xy1 = x1 - y1
    else:
        xy1 = y1 - x1
        
    
if x2 < 0 and y2 >= 0:  
    xy2 = (x2*-1) + y2
elif x2 >= 0 and y2 < 0:
    xy2 = x2 + (y2 * -1)
elif x2 < 0 and y2 < 0:
    if x2 > y2:
        xy2 = x2 - y2
    else:
        xy2 = y2 - x2
elif x2 >= 0 and y2 >= 0:
    if x2 >= y2:
        xy2 = x2 - y2    
    else:
        xy2 = y2 - x2

import math
resultado = math.sqrt(xy1**2 + xy2**2)  

if resultado >= 10:
    print("longe")
else:
    print("perto")
