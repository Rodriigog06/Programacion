cadena=input("Dame un numero: ")
contador=0
cadenas=""
for i in range (len(cadena)-1,0,-1):
    contador+=1
    if contador !=3:
        cadenas=cadena[i]+ cadenas
      
    else:
        contador = 0
        cadenas="." + cadena[i] + cadenas
    

print(cadena[0]+ cadenas)