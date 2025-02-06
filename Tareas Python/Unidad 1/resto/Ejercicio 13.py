def calculadora():
    # leer un caracter
    operador = input ("introduce un operador aritmético (+, -, *, %, /):")

    # leer dos numeros enteros
    try: 
        num1 = int(input("introducir el primer numero entero:"))
        num2 = int(input("introducir el segundo numero entero:"))
    except ValueError :
        print ("introducir numeros enteros validos")
        return
    if operador =="+" : 
        resultado = num1 + num2
        print ("el resultado de {num1} + {num2} es : {resultado}")
    elif operador == "-" :
        resultado = num1 - num2
        print ("el resultado de {num1} - {num2} es : {resultado}")
    elif operador == "*" :
        resultado = num1 * num2
        print ("el resultado de {num1} * {num2} es : {resultado}")
    elif operador == "%" :
        resultado = num1 % num2
        print ("el resultado de {num1} % {num2} es : {resultado}")
    elif operador == "/" :
        if num2 !=0:
            resultado = num1 / num2
            print ("el resultado de {num1} / {num2} es : {resultado}")
        else:
            print ("error: no se puede dividir")
    else:
        print ("error: el caracter introducido no es un operador")
    # llamar a la función
    calculadora()