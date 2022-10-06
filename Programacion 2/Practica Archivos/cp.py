#ejercicio 2 archivos
c = input("Ingrese Ruta de archivo a copiar ")
a = open(c,'r')
b = a.readlines()
d = open("copia.txt", 'w+')
for x in b:
    d.write(x)
d.close()
