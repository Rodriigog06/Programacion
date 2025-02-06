nombrecompleto=input("Dame un nombre y sus apellidos")
tablacadenas=nombrecompleto.split()

for palabra in tablacadenas:
    print(palabra[0].upper()+palabra[1:-1].lower + palabra[-1].upper())