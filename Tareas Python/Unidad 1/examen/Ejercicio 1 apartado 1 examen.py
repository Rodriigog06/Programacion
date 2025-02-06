S ="Si"
N ="No"
incidente=int(input("¿Desea registrar un nuevo incidente? S (para si), N (para no)"))
while incidente ==S:
    nivel=int(input("¿En que nivel ha ocurrido?"))
    E = ("ESO")
    P = ("Post-Obligatoria")
    while nivel == E or nivel == P:
        tipoincidente= int(input("¿Que tipo de incidente ha ocurrido:, tipo de incidente. L(para incidentes leves) o G(para incidentes graves)?")) 
        L= "Leve"
        G= "Grave"
        while tipoincidente== L or tipoincidente==G:
            nuevoincidente=("¿Desea registrar un nuevo incidente? S (para si), N (para no)")
        if tipoincidente !=L or tipoincidente !=G:
            print("¿Que tipo de incidente ha ocurrido:, tipo de incidente. L(para incidentes leves) o G(para incidentes graves)?")
    if nivel != E or nivel !=P:
        print("¿En que nivel ha ocurrido?")
if incidente ==N:
    print("Incidentes registrados")


