def EsMultiplo (num1,num2):
    mult = False
    if num1%num2==0:
        mult = True
    return mult
       

numfuncion = EsMultiplo(int(input("Introduce un numero:")), float(input("Introduce otro numero")))
print(numfuncion)