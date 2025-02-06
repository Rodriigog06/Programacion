num=input("dame un numero: ")
quitar= int(input("¿cuantos numeros quieres quitar?:"))

if quitar < len(num):
    num1=num[quitar:len(num)]
    print("num1")
elif num ==len(num):
    print("La cadena no esta llena")
else:
    print("No se pueden quitar mas digitos de los que contiene el numero")