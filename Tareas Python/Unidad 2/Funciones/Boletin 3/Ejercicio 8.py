import random
def aleatorio():
    numeros=[]
    for veces in range (0,100):
        numeros.append(random.randint(0,1000))
    return numeros
    
def mayor():
   numerosgenerados= aleatorio()
   maximo = max(numerosgenerados)
   return maximo
   
def menor():
   numerosgenerados= aleatorio()
   minimo = min(numerosgenerados)
   return minimo

def suma():
    numerosgenerados= aleatorio()
    total=0
    for numero in numerosgenerados:
        total=total+numero
    return total

def media():
    numerosgenerados= aleatorio()
    total=0
    sumatotal= suma()
    total= sumatotal / 100
    return total

def sustituye(lista1):
    print(lista1)
    numSustituir=int(input("Introduce un numero:"))
    numSustituye=int(input("Introduce el numero a sustituir:"))
    for i in range (len(lista1)):
        if numSustituir==lista1[i]:
            lista1[i]=numSustituye
    return lista1

def imprimeMenu():
    print ("A---Conocer el mayor")
    print ("B---Conocer el menor")
    print ("C---Obtener la suma de todos los numeros")
    print ("D---Obtener la media")
    print ("E---Sustituir el valor de un elemento")
    print ("F---Mostrar todos los numeros")
    respuesta=input("Introduzca una letra")
    while not(respuesta== "A" or  respuesta == "B" 
           or  respuesta == "C" or  respuesta == "D" 
           or  respuesta == "E" or  respuesta == "F"):  
        print ("A---Conocer el mayor")
        print ("B---Conocer el menor")
        print ("C---Obtener la suma de todos los numeros")
        print ("D---Obtener la media")
        print ("E---Sustituir el valor de un elemento")
        print ("F---Mostrar todos los numeros")
    return respuesta
respuesta=imprimeMenu()
match respuesta:
    case "A":
        print (f"El numero mas grande es:",mayor())
    case "B":
        print (f"El numero mas pequeño es:",menor())
    case "C":
        print (f"La suma de los numeros es:",suma())
    case"D":
        print (f"La media de los numeros es:",media())
    case "E":
        print (f"Sustituir el valor de un elemento:",sustituye())
    case"F":
        print (f"Los numeros aleatorios son:",aleatorio())
    case _:
        print("No vale ese carácter")