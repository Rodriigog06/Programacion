def sumaColumnaPares(matriz):
    suma=0
    for numColum in range (len(matriz)):
        if numColum %2==0:
           for elementofila in matriz[numColum]:
               suma= suma + elementofila
    return (suma)

matriz=[[8,1,6],[3,5,7],[4,9,2]]
print(sumaColumnaPares (matriz))