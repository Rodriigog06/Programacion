def calcularMax (numArr):
    max=-99999999
    
    for i in range(len(numArr)):
        if numArr[i]>max:
            max=numArr[i]
    
    return max

arr=[]
while len(arr)<=10:
    num=int(input("dame numeros:"))
    arr.append(num)

print(calcularMax(arr))
