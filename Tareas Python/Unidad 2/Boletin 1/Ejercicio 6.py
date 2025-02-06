from math import pi


def calculaArea (radio):
    area = 2*pi*radio
    return area


def calculaPerimetro (radio):
    perimetro = pi*(radio*radio)
    return perimetro


def calculaAreaYPerimetro(radio):
    area=calculaArea(radio)
    perimetro=calculaPerimetro (radio)
    return [perimetro, area]


radioEntrada = int(input("Dame el radio de la circunferencia: "))
resultado = calculaAreaYPerimetro

print(resultado[0])
print(resultado[1])


