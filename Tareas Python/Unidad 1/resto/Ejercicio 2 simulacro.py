lista= []
num1 = int(input("Dame un numero"))
num2 = int(input("Dame otro numero"))
num3 = int(input("Dame otro numero"))

if num1 and num2 or num1 and num3 or num2 and num3 or num1 and num2 and num3<=0 :
    print("Se acabó el programa")
elif num1 and num2 or num1 and num3 or num2 and num3 or num1 and num2 and num3>0 :
    print(lista)
    if num1 > num2 > num3:
        print(num1, num2, num3)
    if num2 > num1 > num3:
        print(num2, num1, num3)
    if num2 > num3 > num1:
        print(num2, num3, num1)
    if num1 > num3 > num2:
        print(num1, num3, num2)
    if num3 > num2 > num1:
        print(num3, num2, num1)
    if num3 > num1 > num2:
        print(num3, num1, num2)


