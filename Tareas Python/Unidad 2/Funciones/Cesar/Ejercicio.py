abecedario = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
texto = (input("Introduce la cadena a cifrar: "))
espacios =  int (input("Introduce el número de espacios que quieres: "))

while len (texto) > 100:
    texto = (input("Cadena incorrecta. Por favor introduce una que sea inferior a 100 caracteres: "))

while espacios >27:
    espacios =  int (input("Número incorrecto. Por favor introduce una que sea inferior a 27 caracteres: "))
    
def cifradocesar (abecedario,texto,espacios):
    cifrado = []
    
    
    for i in range (len(texto)):
        posicion = abecedario.index(texto[i])
        nuevaposicion = posicion + espacios
        if nuevaposicion > 27:
            nuevaposicion = nuevaposicion - len(abecedario) 
        nuevaletra= abecedario[nuevaposicion]
    
        cifrado.append (nuevaletra)              
    return cifrado

print (cifradocesar(abecedario,texto,espacios))

def descifrado (abecedario, texto, espacios):
    descifrar = []
    
    for i in range (len(texto)):
        posicion = abecedario.index(texto[i])
        nuevaposicion = posicion - espacios
        if nuevaposicion > 27:
            nuevaposicion = nuevaposicion + len(abecedario) 
        nuevaletra= abecedario[nuevaposicion]
    
        descifrar.append (nuevaletra)              
    return descifrar

def imprimeMenu(opcion):
    print("1---- Introducir un nuevo usuario")
    print("2--- Modificar palabra clave de cifrado")
    print("3--- Cifrar un mensaje")
    print("4--- Descifrar un mensaje")
    print("5--- Eliminar usuario")
    print("6--- Terminar")
    respuesta=input("Introduce un numero")

    while respuesta not in ['1','2','3','4','5','6']:
        print("1--- Introducir un nuevo usuario")
        print("2--- Modificar palabra clave de cifrado")
        print("3--- Cifrar un mensaje")
        print("4--- Descifrar un mensaje")
        print("5--- Eliminar usuario")
        print("6--- Terminar")
        respuesta=input("Introduce un numero")
    return opcion

def nuevoUsuario ():
    usuario=[]


