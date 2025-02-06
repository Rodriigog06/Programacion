numeros=[]
num= int(input("Dame un numero (0 finaliza el programa)"))

while num !=0 :
    numeros.append(num)
    num= int(input("Dame un numero (0 finaliza el programa)"))

if len (numeros) ==0:
    print ("No hay numeros para comparar")

else:
    creciente = True
    decreciente = True

    for i in range (1, len(numeros)):
        if numeros[i]< numeros[i-1]:
            creciente = False
        elif numeros[i]> numeros[i-1]:
            creciente = False

    if creciente == True :
        print("Orden Creciente")
    elif decreciente == True :
        print("Orden decreciente")
    else:
        print("No hay orden, desordenados")
