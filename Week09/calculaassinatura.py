import re

def calcula_assinatura(texto):
    """
    Essa função recebe um texto e deve devolver a assinatura
    do texto.
    """
    if type(texto) != list:
        aux = texto
        texto = []
        texto.append(aux)
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))  
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)  
            num_tot_sentencas += 1
            soma_cat_sentencas = soma_cat_sentencas + len(sentencas[i])
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                palavra_i = separa_palavras(str(frases[lin][col]))
                palavras.append(palavra_i)  
                num_tot_frases += 1
                soma_cat_frases = soma_cat_frases + len(str(frases[lin][col]))
        mtrx_para_lista = []  
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                mtrx_para_lista.append(palavras[lin][col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras = soma_comp_palavras + len(str(palavras[lin][col]))
            num_tot_palavras += 1
        as_b = []
        as_b.append(wal(soma_comp_palavras, num_tot_palavras))
        as_b.append(ttr(palavras, num_tot_palavras))
        as_b.append(hlr(palavras, num_tot_palavras))
        as_b.append(sal(soma_cat_sentencas, num_tot_sentencas))
        as_b.append(sac(num_tot_frases, num_tot_sentencas))
        as_b.append(pal(soma_cat_frases, num_tot_frases))
    return as_b  

def wal(soma_comp_palavras, num_tot_palavras):
    if num_tot_palavras != 0:
        wal = soma_comp_palavras / num_tot_palavras
    else:
        wal = 0
    return wal

def ttr(lista_palavras, num_tot_palavras):
    num_pal_dif = n_palavras_diferentes(lista_palavras)
    if num_tot_palavras != 0:
        ttr = num_pal_dif / num_tot_palavras
    else:
        ttr = 0
    return ttr

def hlr(lista_palavras, num_tot_palavras):
    num_pal_uni = n_palavras_unicas(lista_palavras)
    if num_tot_palavras != 0:
        hlr = num_pal_uni / num_tot_palavras
    else:
        hlr = 0
    return hlr

def sal(soma_num_cat, num_sent):
    if num_sent != 0:
        sal = soma_num_cat / num_sent
    else:
        sal = 0
    return sal

def sac(num_tot_frases, num_tot_sentencas):
    if num_tot_sentencas != 0:
        sac = num_tot_frases / num_tot_sentencas
    else:
        sac = 0
    return sac

def pal(soma_cat_frases, num_tot_frases):
    if num_tot_frases != 0:
        pal = soma_cat_frases / num_tot_frases
    else:
        pal = 0
    return pal

def separa_sentencas(texto):
    """
    A função recebe um texto e devolve uma lista das sentenças dentro
    do texto.
    """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    """
    A função recebe uma sentença e devolve uma lista das frases dentro
    da sentença.
    """
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    """
    A função recebe uma frase e devolve uma lista das palavras dentro
    da frase.
    """
    return frase.split()

def n_palavras_unicas(lista_palavras):
    """
    Essa função recebe uma lista de palavras e devolve o numero de palavras
    que aparecem uma única vez.
    """
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    """
    Essa função recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas.
    """
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
