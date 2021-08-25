def é_hipotenusa(a):
    
    cateto1 = 0
    cateto2 = 0

    for i in range(1, a):
        for j in range(1, a):
            if i ** 2 + j ** 2 == a ** 2:
                cateto1 = i
                cateto2 = j
                break
                
    if cateto1 != 0 and cateto2 != 0:
        return True
    else:
        return False
    #print("Cateto1 = %d\nCateto2 = %d" % (cateto1, cateto2))
    
def soma_hipotenusas(n):
    
    #lista = []
    soma = 0
    
    for i in range(2, n+1):
        if é_hipotenusa(i) == True:
            soma += i
    return soma
