cadena= input("Dame un numero")
inicio= int(input("Dame el inicio"))
fin=int(input("Dame el fin"))
if inicio < fin and inicio < len (cadena) and fin < len (cadena) :
    print(cadena[inicio: fin+1])
else:
    print("No se puede")