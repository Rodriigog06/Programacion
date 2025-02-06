cadena= input("Dame una cadena")
letra=input("Que letra cuento")
contador=0
num=input("Si introduce 1 escribirá por pantalla cada carácter de una cadena introducida por teclado. En otro caso, contará el % de veces que aparece un carácter que se ha introducido por teclado")




if num ==1:
    contadora=0
    while contador < len(cadena):
        print(cadena[0+contadora])
        contadora+=1
    print("Termina")

else:
    for c in cadena:
        if c==letra:

            contador+=1
    print("En",cadena, "la letra", letra, "aparece un", contador*100/len(cadena),"%", "veces")
    



