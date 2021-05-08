def empilha(lista,p1,p2):
    lista[p2] = lista[p1]
    del lista[p1]
    return lista