def exponente (num1, num2):
    if num2==0:
        return 1
    resultado=1
    for i in range(1, num2+1):
        resultado=resultado*num1
    return resultado
    

    resultadonum= exponente(5,0)
    print(resultadonum)
    resultadonum= exponente(5,1)
    print(resultadonum)