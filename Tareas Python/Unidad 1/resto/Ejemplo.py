claveusuario = int(input("dame una contraseña"))
match claveusuario:
    case 1234 :
        print("Contraseña correcta")
    case _ :
        print("Contraseña incorrecta")