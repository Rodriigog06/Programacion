cadena=input("Introduce una cadena")
longitud=len(cadena)
while len (cadena)<= 4:
    cadena=input("Introduce una cadena")

else:
    num=input(input("Dime un numero"))
    if num%2==0:
        print((cadena[2]+cadena[4])*longitud)

    if num%3==0:
        print((cadena[1]+cadena[2])*longitud)

    if num%7==0:
        print((cadena[0]+cadena[3])*longitud)
    