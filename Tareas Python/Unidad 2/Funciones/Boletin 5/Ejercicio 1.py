listadodni=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
dni=[]
def validadniespañol (dni):
    #solo nº dni
    numdni=(dni[0:-1])
    if len(numdni) == 7 or len(numdni) == 8:
        #posicion de la letra del dni
        posicionlistado = (int(numdni)%len(listadodni))
        #letra dni
        letradni = listadodni[int(posicionlistado)]
        comprobarletra = dni[-1]

        if letradni == comprobarletra:
            print('El DNI es correcto')
        else: 
            print('No es correcto el DNI')
        return letradni
    else:
        print('la longitud no es correcta')

dni=input('Dime un Dni español')

print(validadniespañol(dni))


listadodni=['x','y','z']
dni=[]
def validadniextranjero (dni):
    #solo nº dni
    numdni=(dni[0:-1])
    if len(numdni) == 7:   
        #posicion de la letra del dni
        posicionlistado = (int(numdni)%len(listadodni))
        #letra dni
        letradni = listadodni[int(posicionlistado)]
        comprobarletra = dni[-1]

        if letradni == comprobarletra:
            print('El DNI es correcto')
        else: 
            print('No es correcto el DNI')
        return dni
    else:
        print('la longitud no es correcta')
    
dni=input('Dime un Dni extranjero')

print(validadniextranjero(dni))