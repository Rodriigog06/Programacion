print("R) Registrar puntuaciones de equipo")
print("L) Listar equipo y su puntuacion por fase")
print("C) Clasificados por fase")
print("S) Salir")
respuesta=input("Introduzca una letra")

if respuesta =="L" or respuesta=="l":
    print ("Inicial")
    print ("Semifinal")
    print ("Final")
    opcion=input("Introduce una fase")

    if opcion != "INICIAL" or opcion !="inicial" or opcion!="SEMIFINAL" or opcion !="semifinal" or opcion!="FINAL" or opcion !="final":
        print("Fase incorrecta")
        print ("Inicial")
        print ("Semifinal")
        print ("Final")
        opcion=input("Introduce una fase")

    else:
        listarPuntuacionesEquipo=input("Imprimiendo las puntuaciones de cada equipo participante en esa fase")

    