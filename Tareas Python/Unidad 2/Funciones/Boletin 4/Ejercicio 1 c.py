
def getColumna (matriz, numFila, numColu):
    columna=[]
    for i in range(0,len(matriz)):
        columna.append(matriz[i][numColu])
    return columna

matriz=[[8,1,6],[3,5,7],[4,9,2]]

print("A: ","getElementoMatriz" (matriz,1,1))
print("B: ","getElementoFila" (matriz,1,2))
print("C: ","getElementocolumna" (matriz,1,0))