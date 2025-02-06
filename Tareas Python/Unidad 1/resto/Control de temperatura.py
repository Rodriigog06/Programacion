# si la temperatura >26 enciende el aire
# si la temperatura es <16 enciende la calefaccion
# distinto, imprime "sin acciones"
# mostrar la temperatura
temp = int (input ("leer el control de temperatura"))
if temp > 26:
    print ("enciende el aire")
elif temp <16:
    print ("enciende la calefaccion")
else:
    print (" sin acciones")
