nombrecompleto=input("Dame un nombre")
tablacadenas=nombrecompleto.split()

for palabra in tablacadenas:
    print(palabra[0].upper()+palabra[1:])


