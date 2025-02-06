def calculaMax (matriz):
    max=-99999
    for elemento in matriz:
        if elemento > max:
            max=elemento
    return max

matriz= [[30, 65, 90, 70], [70, 45, 13,55], [20, 40, 15,10]]
print(calculaMax(matriz))

def calculaMin (matriz):
    min=99999
    for elemento in matriz:
        if elemento < min:
            min=elemento 
    return min

matriz= [[30, 65, 90, 70], [70, 45, 13,55], [20, 40, 15,10]]
print(calculaMin(matriz))