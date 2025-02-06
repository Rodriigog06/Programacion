#Hundir la flota Rodrigo Garcia Gutierrez. Segundo ejercicio




def imprimeMenu():
    print("I) Iniciar partida")
    print("D) Disparar")
    print("R) Imprime resultado actual")
    print("S) Salir")
    respuesta=input("Introduce una letra:")

    while not (respuesta=="I" or respuesta=="D" or respuesta=="R" or respuesta=="S" ) :
        print("I) Iniciar partida")
        print("D) Disparar")
        print("R) Imprime resultado actual")
        print("S) Salir")
        respuesta=input("Introduce una letra válida:")
    return respuesta

lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
barco1=23
barco2=33
barco3=2
barco4=7
barco5=40
barco6=12
barco7=19
barco8=25
barco9=46
barco10=38

barcoshundidos=0
disparos=0

numero=input("Elige un numero del 0 al 49:")
while (numero==barco1 or numero==barco2 or numero==barco3 or numero==barco4 or numero==barco5 or numero==barco6 or numero==barco7 or numero==barco8 or numero==barco9 or numero==barco10):
    print("¡Tocado y hundido! Has acertado en la posicion", (numero))
while numero not in ["23","33","2","7","40","12","19","25","46","38"]:
    print("¡Agua! No habia barco en la posicion" ,(numero))
