import extrai_naipe as enp
import extrai_valor as evr
def lista_movimentos_possiveis(lista,indice):
    naipe = []
    valor = []
    possivel =[]
    i = 0
    while i < len(lista):
        a = enp.extrai_naipe(lista[i])
        b = evr.extrai_valor(lista[i])
        naipe.append(a)
        valor.append(b)
        i+=1
    if indice >= 1:
        if naipe[indice] == naipe[indice-1] or valor[indice] == valor[indice-1]:
            possivel.append(1)
    if indice > 2:
        if naipe[indice] == naipe[indice-3] or valor[indice] == valor[indice-3]:
            possivel.append(3)
    return possivel

