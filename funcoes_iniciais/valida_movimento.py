import movimentos_possiveis
def valida_movimento(lista,indice):
    a = movimentos_possiveis.lista_movimentos_possiveis(lista, indice)
    if a != []:
        return True
    else:
        return False