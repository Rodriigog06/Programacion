def convertirSegundosaHoras(segundos):
    horas = (segundos/3600)
    return horas 

def convertirSegundosaMinutos(segundos):
    minutos=int(segundos/60)
    return minutos

segundos=input("Introduce un numero en segundos:")
horas = int(segundos/3600)

menu = int(input("Introduce una opcion del menu"))
while menu!=4:
    segundos=int(input("Introduce el tiempo en segundo:"))

    resultado = convertirSegundosaHoras (segundos), convertirSegundosaMinutos(segundos)
    if menu ==1:
        print(segundos, "segundos")

    elif menu ==2:
        print(convertirSegundosaMinutos (segundos), "minutos")

    elif menu ==3:
        print(convertirSegundosaHoras (segundos, "horas"))
        
    elif menu ==4:
        print("saliendo del programa")

    