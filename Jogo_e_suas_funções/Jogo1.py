import cria_baralho as cb #função criada para criar o baralho de 52 cartas
import random
import existe_possivel as exp # função criada para verificar se existe movimento possiveis com o baralho no estado atual
import movimentos_possiveis as mp # Devolve os possíveis movimentos, 1 ou 3 ou ambos
import empilhar as emp #É o comando que faz o jogo acontecer, "empilha" uma carta em cima da outra
import valida_movimento as vm #Função que verifica se a carta escolhida tem movimento no baralho atual.
#Pergunta se a pessoa quer jogar
print("Seja bem vindo ao Jogo, vamos as regras:")
print("Existem apenas dois movimentos possíveis:\n ")

print("1. Empilhar uma carta sobre a carta imediatamente anterior\n")
print("2. Empilhar uma carta sobre a terceira carta anterior.\n")

print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n")

print("1. As duas cartas possuem o mesmo valor ou\n")
print("2. As duas cartas possuem o mesmo naipe.\n")
valido = False
quer_jogar = True
while quer_jogar: #faz com que o jogo rode o jogo até que o jogadore responda não 
    while not valido:
        inicio1 = input("quer jogar o jogo?  (sim/nao)  \n")
        if inicio1 == "sim":
            valido = True # variavel para validar se a resposta do jogador é valida (sim ou nao)
            jogar = True # faz com que o jogo rode 
        elif inicio1 == "nao":
            print("Obrigado por visitar o jogo <3")
            quer_jogar = False
            jogar = False
            valido = True
        else:
            print("Resposta inválida, responda com sim ou nao\n")
    if jogar:
        jogar2 = jogar #criada para ditar quando o jogador quer reiniciar o jogo
        #criação do baralho
        a = cb.cria_baralho()
        i = 0
        novo_baralho = [] 
        cartas = []
        #embaralhamento das cartas:
        while i < 52:
            carta = random.choice(a)
            novo_baralho.append(carta)
            a.remove(carta)
            i+=1
        c =len(novo_baralho)
        while jogar2:
            if c == 1:
                print("VOCÊ VENCEU >-< ^_^ :)!")
                validar2 = True
                while validar2:
                    inicio = input("quer jogar o jogo denovo?  (sim/nao)  \n")
                    if inicio == "sim":
                        validar2 = False# Usado para validar a resposta caso o jogador queira jogar denovo ou não
                        valido = True
                        jogar = True
                        jogar2 = False
                        quer_jogar = True
                    elif inicio == "nao":
                        validar2 = False
                        quer_jogar = False
                        jogar = False
                        jogar2 = False
                        valido = True
                    else:
                        print("Resposta inválida, responda com sim ou nao\n")
                        jogar2 = False
                        valido = False
                        validar2 = True               
            else:
                i = 0
                #Definindo as cores das cartas
                VERMELHO = "\033[0;31m"
                AZUL = "\033[0;34m"
                PRETO = "\033[0;30m"
                VERDE = "\033[0;32m"
                RESET = "\033[0;0m" #para que o terminal volte para a cor orginial 
                #Mostrar as cartas na tela
                while i < c:
                    a = i+1
                    ind = len(novo_baralho[i])
                    if novo_baralho[i][ind-1] == "♠":
                        print(VERDE + "{0}. ".format(a) + "{0}".format(novo_baralho[i]) +RESET)
                    elif novo_baralho[i][ind-1] == "♥":
                        print(VERMELHO + "{0}. ".format(a) + "{0}".format(novo_baralho[i])+ RESET)
                    elif novo_baralho[i][ind-1] == "♦":
                        print(AZUL + "{0}. ".format(a) + "{0}".format(novo_baralho[i])+ RESET)
                    elif novo_baralho[i][ind-1] == "♣":
                        print("{0}. ".format(a) + "{0}".format(novo_baralho[i]))
                    i+=1
                condicao = True
                while condicao:
                    indice = int(input("Escolha qual carta quer mover: \n"))
                    if indice > c or indice < 1:
                        errado = True
                    else:
                        errado = False
                    while errado:
                        print("Número inválido, digite outro")
                        indice = int(input("Escolha qual carta quer mover: \n"))
                        if indice > c or indice <1:
                            errado = True
                        else: 
                            errado = False
                    if exp.possui_movimentos_possiveis(novo_baralho):
                        valida = vm.valida_movimento(novo_baralho, indice-1)
                        if valida:
                            condicao = False
                        else:
                            condicao = True
                            print("Não há movimento para essa carta, escolha outra")
                    else:
                        print("Você perdeu :(")
                        condicao = False
                        validar = True
                        while validar:
                            inicio = input("quer jogar o jogo denovo?  (sim/nao)  \n")
                            if inicio == "sim":
                                validar = False
                                valido = True
                                jogar = True
                                jogar2 = False
                                quer_jogar = True
                            elif inicio == "nao":
                                validar = False
                                quer_jogar = False
                                jogar = False
                                jogar2 = False
                                valido = True
                            else:
                                print("Resposta inválida, responda com sim ou nao\n")
                                jogar2 = False
                                valido = False
                                validar = True
                movs = mp.lista_movimentos_possiveis(novo_baralho, indice-1)
                if movs == [1]:
                    emp.empilha(novo_baralho, indice-1, indice-2)
                    c-=1
                elif movs == [3]:
                    emp.empilha(novo_baralho, indice-1, indice-4)
                    c-=1   
                elif movs == [1,3]:
                    print("1.{0}".format(novo_baralho[indice-2]))
                    print("2.{0}".format(novo_baralho[indice-4]))
                    escolha = input("você quer empilhar em qual?  ")
                    if escolha == "1":
                        emp.empilha(novo_baralho, indice-1, indice-2)
                        c-=1      
                    elif escolha == "2":
                        emp.empilha(novo_baralho, indice-1, indice-4)
                        c-=1
if not inicio1 == "nao":
    print("obrigado por jogar o jogo <3 ")