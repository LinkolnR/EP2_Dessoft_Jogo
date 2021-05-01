def cria_baralho():
    lista = []
    carta1 = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    naipe = ["♠","♥","♦","♣"]
    i = 0
    j = 0
    while j <len(naipe):
        while i < len(carta1):
            carta = carta1[i]+naipe[j]
            lista.append(carta)
            i+=1
        i = 0
        j+=1 
    return (lista)
