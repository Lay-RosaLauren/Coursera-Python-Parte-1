def maior_elemento(lista):
    
    maior = lista[0]
    
    for i in lista:
        if maior < i:
            maior = i
    
    return maior

lista = [5, 10, 15, 20, 25, 30]
maior_elemento(lista)
