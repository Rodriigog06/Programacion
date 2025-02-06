num1=int(input("Introduce un primer numero"))
num2=int(input("Introduce un segundo numero"))

if num1>=num2:
    num1=int(input("Introduce un primer numero"))
    num2=int(input("Introduce un segundo numero"))
if num1<num2:
    for i in range (num1, num2, 2):
        print("=====================================")
        print("Impares existen entre"[num1-num2])
        print(":"[i])
        print("En total existen"[i])
        print("numeros impares en el rango")
        print("=====================================")
 