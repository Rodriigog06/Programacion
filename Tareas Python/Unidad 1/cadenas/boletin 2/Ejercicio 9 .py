cadena=input("Introduce una cadena:")

pricar=input("Introduce un caracter a sustituir:")
while len(pricar) !=1:
    print("Introduce un solo caracter.")
    pricar=input("Introduce otro caracter por el que sustituir:")

segcar=input("Introduce otro caracter por el que sustituir:")
while len(segcar)!=1:
    print("Introduce solo un caracter")
    segcar=input("Introduce otro caracter por el que sustituir:")

nuevacadena=cadena.replace(pricar, segcar)

print("La nueva cadena es: ", nuevacadena)