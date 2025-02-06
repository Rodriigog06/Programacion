estaciondelaño = int(input("introduce mes: "))
dia = int(input("introduce dia: "))
match estaciondelaño :
    case 1|2|3:
        if estaciondelaño ==3 and dia >20 :
            print ("es Primavera")
        else:
            print("es Invierno")
    case 4|5|6:
        if estaciondelaño ==6 and dia >20 :
            print("es Verano")
        else: 
            print("es Primavera")
    case 7|8|9:
        if estaciondelaño ==9 and dia >20 :
            print("es Otoño")
        else:
            print ("es Verano")
    case 10|11|12:
        if estaciondelaño ==12 and dia >20 :
            print ("es Invierno")
        else:
            print("es Otoño")


