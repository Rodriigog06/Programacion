def calculamedia (num1,num2):
    media=(num1 + num2)/2
    return media

numdias=int(input("Introduce el numero de dias de los que quieres calcular la media"))

for i in range(0, numdias):
    tempmax=int(input("Dame la temperatura maxima del dia"))
    tempmin=int(input("Dame la temperatura minima del dia"))
    resultadofun=calculamedia (tempmax, tempmin)
    print(resultadofun)  