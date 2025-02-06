random1 = random.randint (0, 10) 
random2 = random.randint (0, 10) 
sumaRandom = random1+random2

suma2 = int(input("dame la suma de estos dos numeros: {random1} + {random2} = "))

while suma2 != sumaRandom :
    suma2 = int(input(f"incorrecto, dame la suma de estos dos numeros: {random1} + {random2} = "))

print(f"¡correcto! La suma de {random1} + {random2} = {sumaRandom}")