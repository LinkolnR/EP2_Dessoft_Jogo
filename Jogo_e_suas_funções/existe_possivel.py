import movimentos_possiveis as mp
def possui_movimentos_possiveis(lista):
    i = 0 
    j = 0 
    while i < len(lista):
        a = mp.lista_movimentos_possiveis(lista, i)
        if a != []:
            j+=1
        i+=1
    if j == 0:
        return False
    else:
        return True