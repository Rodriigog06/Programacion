def devuelveDiagonalSecundaria(matriz):
    columna= len(matriz)-1
    listaDiagonal=[]
    for posfila in range(0,len(matriz)-1,1):
        elemento=(matriz[posfila][columna])
        listaDiagonal.append(elemento)
        columna=columna-1
        
    return listaDiagonal

matriz=[[8,1,6],[3,5,7],[4,9,2]]
print (devuelveDiagonalSecundaria(matriz))