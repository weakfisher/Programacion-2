def inicializaTablero() -> 'list':
    tablero = []
    for i in range(8):

        tablero.append(([" "] * 8   ))
    return tablero


def muestraTablero(tablero: 'list') -> None:
    print("A   B   C   D   E   F   G   H")
    for fila in tablero:

        print(fila[0], '|', fila[1], '|', fila[2],"|", fila[3],"|", fila[4], "|",fila[5],"|", fila[6], "|", fila[7])

def validarJugada(tablero,coordX,coordY, ficha):
    cordenada = tablero[coordX][coordY]
    if cordenada != " " or  not estaEnTablero(coordX, coordY):
        return False #esto indica si ya existe una ficha en dicho lugar

    tablero[coordX][coordY] = ficha
    if ficha == "X":
        otraFicha = "O"
    else:
        otraFicha = "X"

    fichas_giradas = []
    #Test alg
    for xdirect, ydirect in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x = coordX
        y = coordY
        x += xdirect
        y += ydirect

        if estaEnTablero(x , y) and tablero[x][y]== otraFicha: #verifica si hay una ficha de otro color al lado nuestro
            x += xdirect
            y += ydirect
            if not estaEnTablero(x,y):
                continue #verificar
            while tablero[y][x] == otraFicha:
                x += xdirect
                y += ydirect
                if not estaEnTablero(x ,y):
                    break
            if not estaEnTablero (x ,y ):
                continue
            if tablero[y][x] == ficha:
                while True:
                    x -= xdirect
                    y -= ydirect
                    if x == coordX and y == coordY:
                        break
                    fichas_giradas.append([y,x])
    tablero[coordX][coordY] = " "
    if len(fichas_giradas) == 0:
        return False #no es un movimiento valido
    return fichas_giradas

def estaEnTablero(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def tableroValido(tablero):
    tableroVal = inicializaTablero(tablero)
    for x in range(8):
        pass
# VERIFICAR UTILIDAD

def ingresarCoordX(coordX):
    a = ["A","B","C","D","E","F","G","H"]


    for i in a:
        if coordX == i:
            coordFinal = a.index(i)
            return int(coordFinal)

            # VERIFICAR UTILIDAD
def ingresarCoordY(coordY):
    if int(coordY) >= 0 and int(coordY) <= 7:
        return int(coordY)


def contadorPuntos(tablero):
    Xpuntos = 0
    OPuntos = 0
    for x in range(8):
        for y in range(8):
            if tablero[x][y] == "X":
                Xpuntos += 1
            if tablero[x][y] == "O":
                OPuntos += 1
    return {'X':Xpuntos, 'O':OPuntos}

def hacerMovimiento(tablero, ficha, coordX, coordY):
    fichas_giradas = validarJugada(tablero , coordX, coordY, ficha)
    if fichas_giradas == False:
        return False
    tablero[coordY][coordX] = ficha
    for x, y in fichas_giradas:
        tablero[x][y] = ficha
    return True

def jugar():
    tableroPrincipal = inicializaTablero()
    tableroPrincipal[3][3] = "X"
    tableroPrincipal[4][4]= "X"
    tableroPrincipal[3][4] = "O"
    tableroPrincipal[4][3] = "O"

    jugadaNumero = 0

    while True:
        ficha = ["X","O"]
        muestraTablero(tableroPrincipal)

        jugada = str(input("Ingrese Jugada"))
        print( "Turno de", ficha[jugadaNumero % 2])
        hacerMovimiento(tableroPrincipal, ficha[jugadaNumero % 2],ingresarCoordX(jugada[0]),ingresarCoordY(jugada[1]))

        jugadaNumero += 1
