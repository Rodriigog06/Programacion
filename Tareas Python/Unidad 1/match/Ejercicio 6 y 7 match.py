salir = False
while not salir:
    print("====================================")
    print("CALCULADORA")
    print("====================================")
    print("Introduzca + si quiere sumar")
    print("Introduzca - si quiere restar")
    print("Introduzca * si quiere multiplicar")
    print("Introduzca / si quiere dividir")
    print("Introduzca @ para salir del menú")
    print("====================================")

    operador = input("Seleccione una opcion: ")

    if operador == "+" or operador == "-" or operador == "*" or operador == "/" :
        num1 = int(input("Introduce el primer numero: "))
        num2 = int(input("Introduce el segundo numero: "))

        match operador :
            case "+":
                resultado = num1 + num2
                print("El resultado de la suma es:", resultado)
            case "-":
                resultado = num1 - num2
                print("El resultado de la resta es:", resultado)
            case "*":
                resultado = num1 * num2
                print("El resultado de la multiplicacion es:", resultado)
            case "/":
                if num2 !=0:
                    resultado = num1 / num2
                    print("El resultado de la division es:", resultado)
                else:
                    print("Error: no se puede dividir entre cero")
            case "@":
                salir = True
                print("Saliendo del menu...")
    else:
        print("ERROR. Caracter no reconocido")

