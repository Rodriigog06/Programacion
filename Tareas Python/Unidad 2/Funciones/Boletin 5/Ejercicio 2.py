def imprimeMenu():
    print("1----Asignar coche a surtidor y repostar")
    print("2----Consultar estado de surtidores")
    print("3----Asignar precio a la gasolina")
    print("4----Asignar precio al diesel")
    print("5----Recargar surtidor")
    print("6----Cerrar el programa y salir")
    print("7----")
    print("8----")
    respuesta=input("Introduzca un numero")
    while not(respuesta==1 or respuesta==2
              or respuesta==3 or respuesta==4
              or respuesta==5 or respuesta==6):
        print("1----Asignar coche a surtidor y repostar")
        print("2----Consultar estado de surtidores")
        print("3----Asignar precio a la gasolina")
        print("4----Asignar precio al diesel")
        print("5----Recargar surtidor")
        print("6----Cerrar el programa y salir")
        print("7----")
    return respuesta
respuesta=imprimeMenu()
match respuesta:
    case "A":
        print(f"El suritdor asignado es:")
    case "B":
        print(f"El estado de los surtidores es:")
    case "C":
        print(f"El precio de la gasolina es:")
    case "D":
        print(f"El precio del diesel es:")
    case "F":
        print(f"Recarga de resurtidor realizada:")
    case _:
        print("No vale ese caracter")   

