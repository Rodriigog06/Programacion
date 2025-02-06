print("R) Registrar puntuaciones de equipo")
print("L) Listar equipo y su puntuacion por fase")
print("C) Clasificados por fase")
print("S) Salir")
respuesta=input("Introduzca una letra")    

if respuesta =="R" or respuesta =="r":
        print ("¿En que fase quieres registrar las puntuaciones?")
        print ("Inicial")
        print ("Semifinal")
        print ("Final")
        opcion=input("Introduce una fase")

        if opcion =="INICIAL" or opcion =="inicial":
                registroPuntuaciones1=input("Introduce los datos de cada equipo. Estas en la fase inicial, introduce los datos de 8 equipos iniciales de la siguiente manera: nombre del equipo: puntuacion obtenida")
                faseInicial=registroPuntuaciones1
        
        if opcion=="SEMIFINAL" or opcion =="semifinal":
                registroPuntuaciones2=input("Introduce los datos de cada equipo. Estas en la fase semifinal, introduce los datos de los 4 equipos semifinalista de la siguiente manera: nombre del equipo: puntuacion obtenida")
                faseSemifinal=registroPuntuaciones2

        if opcion=="FINAL" or opcion =="final":
                registroPuntuaciones3=input("Introduce los datos de cada equipo. Estas en la fase final, introduce los datos de los 2 equipos finalistas de la siguiente manera: nombre del equipo: puntuacion obtenida")
                faseInicial=registroPuntuaciones3

        else:
            print("Fase incorrecta")
            print ("¿En que fase quieres registrar las puntuaciones?")
            print ("Inicial")
            print ("Semifinal")
            print ("Final")
            opcion=input("Introduce una fase")
                    