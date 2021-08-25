def éPrimo(k):

    divisores = 0
    for i in range(1,k):
        if k % i == 0:
            divisores += 1
    if divisores >= 2:
        return False
    else:
        return True

def n_primos(n):

    n_primos = 0

    for i in range(2, n+1):
        if éPrimo(i) == True:
            n_primos += 1
    
    return n_primos
