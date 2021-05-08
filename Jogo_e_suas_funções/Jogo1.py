import cria_baralho as cb
import random
import existe_possivel as exp
import movimentos_possiveis as mp
import empilhar as emp
import valida_movimento as vm
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
while quer_jogar:
    while not valido:
        inicio = input("quer jogar o jogo?  (sim/nao)  \n")
        if inicio == "sim":
            valido = True
            jogar = True
            quer_jogar = False
        elif inicio == "nao":
            print("Obrigado por visitar o jogo <3")
            quer_jogar = False
            jogar = False
            valido = True
        else:
            print("Resposta inválida, responda com sim ou nao\n")
    if jogar:
        jogar2 = jogar
        #criação do baralho
        a = cb.cria_baralho()
        i = 0
        novo_baralho = [] 
        cartas = []
        #embaralhamento das cartas:
        while i < 3:
            carta = random.choice(a)
            novo_baralho.append(carta)
            a.remove(carta)
            i+=1
        c =len(novo_baralho)
        while jogar2:
            if c == 1:
                print("VOCÊ VENCEU >-< ^_^ :)!")
                inicio = input("quer jogar o jogo denovo?  (sim/nao)  \n")
                if inicio == "sim":
                    valido = True
                    jogar = True
                    jogar2 = False
                    quer_jogar = True
                elif inicio == "nao":
                    quer_jogar = False
                    jogar = False
                    jogar2 = False
                    valido = True
                else:
                    print("Resposta inválida, responda com sim ou nao\n")
                    jogar2 = False
                    valido = False                
            else:
                i = 0
                #Definindo as cores das cartas
                VERMELHO = "\033[0;31m"
                AZUL = "\033[0;34m"
                PRETO = "\033[0;30m"
                VERDE = "\033[0;32m"
                RESET = "\033[0;0m"
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
                    indice = int(input("Escolha qual carta quer mover: "))
                    if indice > c or indice < 1:
                        errado = True
                    else:
                        errado = False
                    while errado:
                        print("Número inválido, digite outro")
                        indice = int(input("Escolha qual carta quer mover: "))
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
                        # jogar = False
                        # quer_jogar = True
                        condicao = False
                        inicio = input("quer jogar o jogo denovo?  (sim/nao)  \n")
                        if inicio == "sim":
                            valido = True
                            jogar = True
                            jogar2 = False
                            quer_jogar = True
                        elif inicio == "nao":
                            quer_jogar = False
                            jogar = False
                            jogar2 = False
                            valido = True
                        else:
                            print("Resposta inválida, responda com sim ou nao\n")
                            jogar2 = False
                            valido = False
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
print("obrigado por jogar o jogo <3 ")