num6=input("dame un numero: ")
numDel= int(input("¿cuantos numeros quieres quitar?:"))

if numDel > len(num6):
    subStr=num6[0 : len(num6)-numDel]
    print(subStr)

if numDel == len(num6):
    print("La cadena esta vacia")
else:
    print("No se pueden quitar mas digitos de los que contiene el numero")