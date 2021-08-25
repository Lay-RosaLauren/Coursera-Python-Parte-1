
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
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
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.'''

    # Sab=∑i=16||fi,a−fi,b||6
    somatoria = 0
    for traco_linguistico in range(len(as_a)):
        somatoria = somatoria + abs(as_a[traco_linguistico] - as_b[traco_linguistico])
    return somatoria / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)

    lista_frases = []
    for s in sentencas:
        frases_separadas = separa_frases(s)
        # separa_frases retorna um item de lista para cada sentença
        # e esses itens são unidos em uma única lista, frases
        for frases in frases_separadas:
            lista_frases.append(frases)

    lista_palavras = []
    for f in lista_frases:
        palavras_separadas = separa_palavras(f)
        for palavras in palavras_separadas:
            lista_palavras.append(palavras)
    assinatura = []

    assinatura.append(tamanho_medio_palavras(lista_palavras))
    assinatura.append(relacao_type_token(lista_palavras))
    assinatura.append(razao_hapax_legomana(lista_palavras))
    assinatura.append(tamanho_medio_de_sentenca(sentencas))
    assinatura.append(complexidade_de_sentenca(lista_frases, sentencas))
    assinatura.append(tamanho_medio_de_frase(lista_frases))

    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valor = ass_cp[0]
    for x in range(len(ass_cp)):
        if ass_cp[x] < valor:
            valor = ass_cp[x]
            indice = x
    return indice

# Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras:
def tamanho_medio_palavras(palavras):
    tamanho_das_palavras = 0
    total_de_palavras = len(palavras)
    for palavra in palavras:
        tamanho_das_palavras = tamanho_das_palavras + len(palavra)

    return tamanho_das_palavras/total_de_palavras

# Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
def relacao_type_token(palavras):
    return n_palavras_diferentes(palavras) / len(palavras)

# Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
def razao_hapax_legomana(palavras):
    return n_palavras_unicas(palavras) / len(palavras)

# Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número
# de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
def tamanho_medio_de_sentenca(sentencas):
    caracteres_sentenca = 0
    for sentenca in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(sentenca)
    return caracteres_sentenca / len(sentencas)

# Complexidade de sentença é o número total de frases divido pelo número de sentenças.
def complexidade_de_sentenca(lista_frases, sentencas):
    return len(lista_frases) / len(sentencas)

# Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo
# número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
def tamanho_medio_de_frase(lista_frases):
    caracteres_frase = 0
    for frases in lista_frases:
        caracteres_frase = caracteres_frase + len(frases)
    return caracteres_frase / len(lista_frases)

def main():
    assinatura_principal = le_assinatura()
    textos = le_textos()
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    assinaturas_comparadas = []
    for assinatura in assinaturas:
        assinaturas_comparadas.append(compara_assinatura(assinatura_principal, assinatura))

    infectado = avalia_textos(textos, assinaturas_comparadas)
    print("O autor do texto", infectado, "está infectado com COH-PIAH.")

main()
