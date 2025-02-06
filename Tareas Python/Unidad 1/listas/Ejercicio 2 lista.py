dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(dias[4:6])
import random

numero = ["1", "2", "3", "4", "5", "6", "7", "8"]
numero.append (random.randint (0, 8))
for i in range (0,8):
    numero.append (random.randint (0, 8))
print (numero)

lista = []
for i in range (0,61,3):
        lista.append(i)
print (lista[0:21])

