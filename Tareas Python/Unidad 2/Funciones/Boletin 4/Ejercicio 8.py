def calculaMaxPorFila (matriz, numFila):
    maximo=-99999
    fila= matriz[numFila]
    for elemento in fila:
        if elemento > max:
            max=elemento
    return max  

    
matriz=[[8,1,6,3],[3,5,7,2],[4,9,2,1]]
numFila=2
print(calculaMaxPorFila (matriz,numFila))