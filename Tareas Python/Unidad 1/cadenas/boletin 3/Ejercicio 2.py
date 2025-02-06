contrasena= input("dame una contraseña")
clave= input("Adivina mi contraseña")
while clave!=contrasena:
    print("Fallaste, la contraseña tiene" ,len(contrasena), " digitos")
    print("El primer caracter es ", contrasena[0])
    print("El ultimo caracter es ", contrasena[len(contrasena)-1])
    clave= input("Adivina mi contraseña")
print("¡Acertaste!")







