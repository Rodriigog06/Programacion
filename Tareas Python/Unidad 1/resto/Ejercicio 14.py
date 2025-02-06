def calificacion_a_letra (calificacion) :
    if 90 <= calificacion <= 100:
        return "A"
    elif 80 <= calificacion <= 90:
        return "B"
    elif 70 <= calificacion <= 80:
        return "C"
    elif 60 <= calificacion <= 70:
        return "D"
    elif 50 <= calificacion <= 60:
        return "F"
    else:
        return "calificacion no valida"
# solicitar al usuario que ingrese la calificacion
try:
    calificacion = float(input("ingresa la calificacion del examen"))
    letra = calificacion_a_letra (calificacion)
    print ("la calificacion equivalente en letras es {letra}")
except ValueError : 
    print ("por favor, ingresar un numero valido")