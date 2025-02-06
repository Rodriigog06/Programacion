def convertirespaciado (cadena):
    cadenaResultado=""
    for c in cadena:
        if c!="":
            cadenaResultado = cadenaResultado +c+""
    return cadenaResultado

cadenaentrada=input("Dame una cadena")
print(convertirespaciado("Hola, tú"))