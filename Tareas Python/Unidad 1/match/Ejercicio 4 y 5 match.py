habitacion = int(input("Introduce un número de habitacion"))

while habitacion !=0 : 
    match habitacion :
        case "1" :
            print("La habitacion azul tiene 2 camas y esta en la primera planta")
        case "2" :
            print("La habitacion roja tiene 1 cama y esta en la primera planta")
        case "3" :
            print("La habitacion verde tiene 3 camas y esta en la segunda planta")
        case "4" :
            print("La habitacion rosa tiene 2 camas y esta en la segunda planta")
        case "5" :
            print("La habitacion gris tiene 1 camas y esta en la tercera planta")
    habitacion = int(input("Introduce un número de habitacion"))