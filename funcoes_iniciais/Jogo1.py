import cria_baralho as cb
import random
import existe_possivel as exp
import movimentos_possiveis as mp
import empilhar as emp
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
# if jogar:
# a = cb.cria_baralho()
# i = 0
# novo_baralho = [] 
# cartas = []
# #embaralhamento das cartas:
# while i < 52:
#     carta = random.choice(a)
#     novo_baralho.append(carta)
#     a.remove(carta)
#     i+=1
# c =len(novo_baralho)
# print(novo_baralho)
# print(c)
# while jogar:


