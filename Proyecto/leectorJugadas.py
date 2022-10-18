#pide un archivo para abrir y guarda dicho archivos

def abrirArchivo():

    while True:
        try:
            archivo_entrada = open(input("Ingrese ruta de archivo a abrir: "),"r+")
            return archivo_entrada
        except:
            print("Error al intentar abrir")
            break
def leerArchivo():
    entrada = input("Ingrese ruta de archivo a abrir: ")
    contenido = open(entrada,'r+')
    nombreFicha = []
    contador= 0
    while contador < 2:
        #Lee las 2 primeras filas y guarda el nombre y la ficha que usan en un lista
        contador += 1
        nombreFicha += [contenido.readline().split(",")]

    fichaPrimera = contenido.readline() #guarda la ficha que empieza

    linea = contenido.readline()
    jugadas = [linea ] #guarda en una lista todas las jugadas
    while linea !="":
        #agarra 1 linea de mas
        linea = contenido.readline()
        jugadas += [linea]


    datos = [nombreFicha, fichaPrimera, jugadas]
    print(datos)
    contenido.close()
