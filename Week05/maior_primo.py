def éPrimo(k):
    divisores = 0
    for divisor in range(1, k):
        if k % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
          break
    if divisores > 1:
        return False
    else:
        return True

def maior_primo(x):
    maior_primo = x
    i = 0
    while i <= x:
        if éPrimo(i):
            maior_primo = i
        i = i + 1
    return maior_primo
