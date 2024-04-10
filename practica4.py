
def ordenar(l, orden):
    lista = l[:]
    limite = len(lista) - 1
    if (orden == "ASC"):
        for x in range(0, limite):
            for y in range(0,limite):
                if lista[y] > lista[y+1]:
                    aux = lista[y]
                    lista[y] = lista[y+1]
                    lista[y+1] = aux   
    elif (orden == "DESC"):
        for x in range(0, limite):
            for y in range(0,limite):
                if lista[y] < lista[y+1]:
                    aux = lista[y]
                    lista[y] = lista[y+1]
                    lista[y+1] = aux 

    return lista

temperatura = [30,125,-3,100,25,-12,-50,1,0,4,6,54,33,65,124,-87,-32,-65,-19,754,26,64,22,70,32,13,74,47,-56,-8,-9,-54]
print(temperatura)
print('----------------------------------------------------------------------------------------------------------------------------------------')
lista_ordenada = ordenar(temperatura, "ASC")
print(lista_ordenada)
print('----------------------------------------------------------------------------------------------------------------------------------------')
lista_ordenada = ordenar(temperatura, "DESC")
print(lista_ordenada)
