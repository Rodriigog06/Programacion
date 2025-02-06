horario = int(input("Dia de la semana")).upper()
match horario :
    case "Lunes":
        print ("8:00 A 11:00  Lenguaje de Marcas")
    case "Martes":
        print("8:00 a 9:00  Programación")
        print("10:00 a 11:00  Entorno de desarrollo")
    case "Miercoles":
        print("8:00 a 9:00  Programación")
        print("10:00 a 11.00  Base de datos")
    case "Jueves" :
        print("8:00 a 9:00  Programación")
        print("10:00 a 11:00  Itinerario personal")
    case "Viernes" :
        print("8:00 a 9:00  Programación")
        print("10:00 a 11:00  Base de datos")
    case "SABADO  DOMINGO" :
        print("Dia de descanso")