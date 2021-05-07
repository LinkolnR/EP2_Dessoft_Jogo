import cria_baralho as cb
import random
import existe_possivel as exp
import movimentos_possiveis as mp
import empilhar as emp
import valida_movimento as vm
#Pergunta se a pessoa quer jogar
valido = False
while not valido:
    inicio = input("quer jogar o jogo?  (sim/nao)")
    if inicio == "sim":
        valido = True
        jogar = True
    elif inicio == "nao":
        jogar = False
        Valido = True
    else:
        print("Resposta inválida, responda com sim ou nao")
if jogar:
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
    while jogar:
        i = 0
        #Mostrar as cartas na tela
        while i < c:
            a = i+1
            print("{0}. {1}".format(a,novo_baralho[i]))
            i+=1
        condicao = True
        while condicao:
            errado = False
            indice = int(input("Escolha qual carta quer mover: "))
            if indice > c or indice < 1:
                errado = True
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
                jogar = False
                condicao = False



        

