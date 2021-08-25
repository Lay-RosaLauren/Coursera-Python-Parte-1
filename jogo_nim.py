def partida():
    # Solicita os valores de n e m
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Define um controlador para quem irá começar o jogo
    x = n % (m + 1)
    # Define um controlador para mensagem que avisa quem irá começar
    primeira_vez_usuario = False
    primeira_vez_computador = False

    if x != 0: # Define que o computador irá começar
        pcJoga = True
        primeira_vez_computador = True # Define que é a primeira jogada do computador
    if x == 0: # Define que o usuário irá começar
        pcJoga = False
        primeira_vez_usuario = True # Define que é a primeira jogada do usuário
    # Enquanto tiver peças(n) no jogo...
    while n > 0:
        if pcJoga == True: # Verifica se o computador começa
            if primeira_vez_computador == True: # Verifica se é a primeira vez do computador
                print("")
                print("Computador começa!")
                print("")
            primeira_vez_computador = False # Define que o computador já jogou a primeira vez
            # Variavel recebendo retorno do número de peças que o computador tirou
            vlr_tirado = computador_escolhe_jogada(n,m)
            # Define que é a vez do usuário
            pcJoga = False
            # Definindo se a mensagem é ficará no singular ou no plural
            if vlr_tirado == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou ",vlr_tirado," peças.")
        else: # Se não for o computador quem começa, então é o usuário...
            # Verifica se é a primeira vez do usuário
            if primeira_vez_usuario == True:
                print("")
                print("Voce começa!")
                print("")
            primeira_vez_usuario = False # Define que o usuário já jogou a primeira vez
            # Variavel recebendo retorno do número de peças que o usuário tirou
            vlr_tirado = usuario_escolhe_jogada(n,m)
            # Define que é a vez do computador
            pcJoga = True
            # Definindo se a mensagem é ficará no singular ou no plural
            if vlr_tirado == 1:
                print("Você tirou uma peça")
            else:
                print("Voce tirou",vlr_tirado,"peças.")
        n = n - vlr_tirado # Remove do tabuleiro as respectivas peças tirada de cada rodada.
        # Para não mostrar que restam 0 peças
        if n > 0:
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
    # Verifica quem jogou por último, e mostra a mensagem respectiva
    if pcJoga == True:
        print("Fim do jogo! Você ganhou!")
        print("")
        return 1 # ID para contabilizar quantas partidas o usuário ganhou no campeonato
    else:
        print("Fim do jogo! O computador ganhou!")
        print("")
        return 0 # ID para contabilizar quantas partidas o computador ganhou no campeonato


# Função que retorna quantas peças o usuário irá tirar do tabuleiro
def usuario_escolhe_jogada(n,m):
    vlr_tirado = 0
    # Enquanto o usuário não digitar um valor válido, ficará preço aqui
    while vlr_tirado == 0:
        vlr_tirado = int(input("Quantas peças você vai tirar?"))
        # Verifica se o valor digitado pelo usuário é valido
        if vlr_tirado > n or vlr_tirado > m or vlr_tirado < 1 :
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            vlr_tirado = 0 # Se for inválido mostra a msg e retorna para o loop
    return vlr_tirado # Se não, retorna o valor tirado


# Função que retorna quantas peças o computador irá tirar do tabuleiro
def computador_escolhe_jogada(n,m):
    if n <= m: # Se o numero de peças for menor que o máximo
        return n # Apenas retorna o mesmo numero de peças para tirar e ganhar logo
    else:
        sobrou = n % (m+1) # sobrou recebe o resto da divisão
        if sobrou > 0:  # Já que não é menor que m, e maior que 0 então...
            return sobrou # retorne o resto
        return m # Se não, retorne o máximo de peças possíveis


# Função que chama partida 3 vezes
def campeonato():
    # Define um controle de placar
    computador = 0
    usuario = 0
    # Define um controle de partidas
    i = 1
    for _ in range(3):
        print("**** Rodada",i,"****")
        print("")
        id_ganhou = partida()
        i = i + 1 # Conta as partidas
        if id_ganhou == 1:
            usuario = usuario +1 # Conta pontos para usuário no placar
        else:
            computador = computador + 1 # Conta pontos para o computador no placar
    print("**** Final do campeonato! ****")
    # Mostra os respectivos placares...
    print("Placar: Você",usuario,"X",computador,"Computador")

# O programa começa aqui, o usuário irá definir a modalidade
escolha = 0
while escolha == 0:
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    escolha = int(input())
    if escolha == 1:
        partida() #Inicia uma partida
        break
    elif escolha == 2:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato() # Inicia um campenato
        break
    else:
        print("Escolha uma opção válida!")
        print("")
        escolha = 0 # Volta para o loop, enquanto não escolher 1 ou 2
