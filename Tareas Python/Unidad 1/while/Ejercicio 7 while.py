import random 
numero = random.randint (1, 10) 
intento= int(input("introduce tu adivinanza"))
while numero != intento :
    intento= int(input("introduce tu adivinanza"))
print("Has adivinado el numero", numero)