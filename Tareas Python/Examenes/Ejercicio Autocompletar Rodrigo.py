#Autocompletar Rodrigo Garcia Gutierrez. Primer ejercicio

lista=["Core i9", "Ryzen 9", "core i7", "Ryzen 5", "fury Beast", "Vengeance LPX", "trident Z5", "Ballistix Sport", "980 PRO", "Black SN850X", "barracuda HDD", "MX500 SSD", "geForce RTX", "radeon RX", "GeForce GTX", "Radeon 6600",  "ROG STRIX", "MPG B550", "Aorus X570", "steel legend" ]
letra=input("Introduce una letra")
listaA="Aorus X570"
listaC="Core i9","core i7"
listaR="Ryzen 9","Ryzen 5","radeon RX","Radeon 6600",  "ROG STRIX"
listaF="fury Beast",
listaB="Ballistix Sport","Black SN850X", "barracuda HDD"
listaV="Vengeance LPX"
listaT="trident Z5"
listaM="MX500 SSD","MPG B550"
listaG="geForce RTX", "GeForce GTX"
listaP="980 PRO"
listaS="steel legend"

if letra=="a" or "A":
    print(listaA)
elif letra=="c" or "C":
    print(listaC)
elif letra=="r" or "R":
    print(listaR)
elif letra=="f" or "F":
    print(listaF)
elif letra=="b" or "B":
    print(listaB)
elif letra=="v" or "V":
    print(listaV)
elif letra=="t" or "T":
    print(listaT)
elif letra=="m" or "M":
    print(listaM)
elif letra=="g" or "G":
    print(listaG)
elif letra=="p" or "P":
    print(listaP)
elif letra=="s" or "S":
    print(listaS)
elif letra not in ["a","A","c","C","r","R","f","F","b","B","v","V","t","T","m","M","g","G","p","P","s","S"]:
    listavacia=[]
    print (listavacia)

letras3=input("Introduce las 3 primeras letras de una plabra de la lista")
listaRad="radeon RX", "Radeon 6600"
listaCor="Core i9","core i7"
listaRyz="Ryzen 9","Ryzen 5"
listaPro="980 PRO"
listaSte="steel legend"
listaTri="trident Z5"
listaGeF="geForce RTX", "GeForce GTX"
listaMXS="MX500 SSD"
listaMPG="MPG B550"
listaVen="Vengeance LPX"
listaAor="Aorus X570"
listaROG="ROG STRIX"
listaBal="Ballistix Sport"
listaBla="Black SN850X",
listaBar="barracuda HDD"
listaFur="fury Beast",

if letras3=="Rad":
    print(listaRad)
elif letras3=="Cor":
    print(listaCor)
elif letras3=="Ryz":
    print(listaRyz)
elif letras3=="Fur":
    print(listaFur)
elif letras3=="Bal":
    print(listaBal)
elif letras3=="Ven":
    print(listaVen)
elif letras3=="Tri":
    print(listaTri)
elif letras3=="MXS":
    print(listaMXS)
elif letras3=="MPG":
    print(listaMPG)
elif letras3=="GeF":
    print(listaGeF)
elif letras3=="Pro":
    print(listaPro)
elif letras3=="Ste":
    print(listaSte)
elif letras3=="Bla":
    print(listaBla)
elif letras3=="Bar":
    print(listaBar)
elif letras3=="Aor":
    print(listaAor)
elif letras3=="ROG":
    print(listaROG)

elif letras3 not in ["Rad","Cor","Ryz","Fur","Bal","Ven","Tri","MXS","MPG","GeF","Pro","Ste","Bla","Bar","Aor","ROG"]:
    listavacia=[]
    print (listavacia)




















    
