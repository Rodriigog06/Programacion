def LetraA (lista):
    contador=0
    letra='a'
    for palabra in lista:
        for caracter in palabra:
           if caracter==letra:
                contador+=1
    return contador
nombre= input('Dime tu nombre:')
apellido1= input('Dame tu primer apellido:')
apellido2= input('Dame tu segundo apellido:')
lista = [nombre, apellido1, apellido2]
print(LetraA(lista))