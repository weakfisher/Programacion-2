
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
        if linea !="z":
            linea = contenido.readline()
            jugadas += [linea]


    datos = [nombreFicha, fichaPrimera, jugadas]
    print(datos)
    return datos
    contenido.close()










#Crea una estructura de tablero
def crearTablero():
    tablero =[]
    for i in range(8):
        tablero.append([" "]*8)
    return tablero
#Dibuja el tablero
def dibujarTablero(tablero):
    print("    A    B     C    D    E    F    G    H")

    for x in range(8):
        print(x+1, end=" ")
        for y in range(8):
            print("| ",tablero[y][x], end=" ")
        print("|")


# validarMovimiento
#Valida si el movimiento es valido
#Devuelve falso si el movimiento no es valido
#devuelve una lista con las fichas que se darian vuelta si dicho movimiento es valido
def validarMovimiento(tablero, ficha, coordX, coordY):
    x = letraNum(coordX)
    y = int(coordY)-1
    if   estaEnTablero(coordX,coordY):
        return False
    tablero[x][y]=ficha[0]
    piezaGiradas = []
    direcciones =  [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for xdirect,ydirect in direcciones:
        x += xdirect
        y += ydirect
        if estaEnTablero(x,y) and tablero[x][y] == ficha[1]:
            x += xdirect
            y += ydirect
            if estaEnTablero(x,y):
                continue
            while tablero[x][y] == fichas[1]:
                x += xdirect
                y += ydirect
                if not estaEnTablero(x,y):
                    break
            if tablero[x][y] == ficha[0]:
                while True:
                    x -= xdirect
                    y -= ydirect
                    if x== letraNum(coordX) and y== int(coordY):
                        break
                    piezaGiradas.append([x,y])
    tablero[letraNum(coordX)][int(coordY)]
    return piezaGiradas


# pregunta si esta en el tablero en caso de que no devuelve false
def estaEnTablero(coordX,coordY):
    if validarCoordX(coordX) and validarCoordY(coordY):
        return True
    else:
        return False
#estaEnTablero
#pregunta si esta en el tablero la coord X
# string -> int / True
# any -> False / false
def validarCoordX(coordX):
    a = ["A","B","C","D","E","F","G","H"]


    for i in a:
        if type(coordX) == str:
            if coordX.upper() == i :
                coordFinal = a.index(i)
                return True
    else: return False


#pregunta si esta en el tablero la coord Y
def validarCoordY(coordY):
    if type(coordY)== int:
        return coordY >= 0 and coordY <=7
    else:
        return False

#trasnforma la letra en su equivalente numerico
def letraNum(coordX):
    a = ["A","B","C","D","E","F","G","H"]


    for i in a:
        if type(coordX) == str:
            if coordX.upper() == i :
                coordFinal = a.index(i)
                return int(coordFinal)

#Pregunta quien va primero y en caso de que no sea valido devuelve False
def quienVaPrimero(nombreFicha):

    if nombreFicha[0] =="B" :
        return  ["X","O"]
    elif nombreFicha[0] == "N":
        return ["O","X"]
    else:
        return False


def jugar():
    tableroPrincipal = crearTablero()
    tableroPrincipal[4][3] = 'X'
    tableroPrincipal[4][4] = 'O'
    tableroPrincipal[3][3] = 'O'
    tableroPrincipal[3][4] = 'X'
    datos = leerArchivo()
    fichas= quienVaPrimero(datos[1])
    turno =fichas[0]
    jugadas =  sacaLista(datos[2])

    if turno == "X":
        for i in jugadas:
            tablero = validarMovimiento(tableroPrincipal,fichas,i[0],i[1])
        print(tablero)
#funcion que toma jugada y evalua su validez
    #si es valida sigue
    #si NO es valida corta y muestra tablero

    #funcion que toma jugada y evalua su validez
        #si es valida sigue
        #si NO es valida corta y muestra tablero


    print(dibujarTablero(tableroPrincipal))
listD = ['D6\n', 'C4\n', 'G5\n', 'F5\n', '']
def sacaLista(lista):
    listaF = lista[:-1]
    return listaF
