expresion = input("Ingrese expresion a buscar :")
archivo = input("Ingrese archivo :")
a = open(archivo,'r')


contador_lineas = 0
lineasEcontradas = []
for i in a:
    contador_lineas += 1
    linea = i.rstrip()
    separado =linea.split(" ")
    if expresion in separado:
        print("se encontro la expresion en ",linea," - ",contador_lineas)

print("la expresion no se encuentre en este documento")
