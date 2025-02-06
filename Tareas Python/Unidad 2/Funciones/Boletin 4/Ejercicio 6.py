def sumaColumna(matriz, numColum):
    suma=0
    columna=matriz[numColum]
    for i in columna:
        suma=i+suma
    return (suma)

matriz=[[8,1,6],[3,5,7],[4,9,2]]
print(sumaColumna (matriz,1))