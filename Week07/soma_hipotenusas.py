def soma_hipotenusas(n):
    soma = 1
    hip = 0
    while soma <= n:
        if é_hipotenusa(soma):
            hip += soma
        soma += 1
    return hip

def é_hipotenusa(n):
    from math import sqrt
    i = 1
    j = 1
    hip = False
    while i <= n and not hip:#loop i
        while j <= n and not hip: #loop j
            hipotenusa = sqrt(i ** 2 + j ** 2)
            if n == hipotenusa:
                hip = True
            j += 1
        j = 1
        i += 1
    return hip
    


    

    
   
   
