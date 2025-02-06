def invierteLista (lista):
    print(lista)
    for lista in range (len(lista),0,-1):
        print(lista)
    return lista

def construyeLista(numelem):
    listanum=[]
    for veces in range (0,numelem,1):
        numero=input("Introduce un numero")
        listanum.append(numero)
    return listanum


veces=int(input("Dime cuantos numeros quieres añadir"))
lista1=construyeLista(veces)

assert(len(lista1)==veces)

lista2=invierteLista(lista1)
assert (len(lista1)==len(lista2))


