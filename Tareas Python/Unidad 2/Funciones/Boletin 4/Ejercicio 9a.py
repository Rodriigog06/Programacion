def devuelveDiagonalPrincipal(matriz):
    columna=0
    fila=0
    listaDiagonal=[]
    for filas in matriz:
        elemento=(matriz[fila][columna])
        listaDiagonal.append(elemento)
        columna=columna+1
        fila=fila+1


    return listaDiagonal

matriz=[[8,1,6],[3,5,7],[4,9,2]]
print (devuelveDiagonalPrincipal(matriz))