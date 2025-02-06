def esCuadrada(matriz):
    cuadrada=True
    fila=len(matriz)
    columna=len(matriz[0])
    if fila==columna:
        return True
    else:
        cuadrada=False
        return False

matriz=[[8,1,6],[3,5,7],[4,9,2]]
print (esCuadrada(matriz))