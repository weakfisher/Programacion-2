from random import *
import random
#generar un board 3x3
#preguntar por un input
#checkear si gano o empato
#imprimir board
#cambiar de jugador
#preguntar por un input
#checkear si gano o empato
#imprimir board

def generarBoard():
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    return board

def mostrarTablero(board):
    i=0
    while i< 9:
        print(board[i],board[i+1],board[i+2])
        i += 3

def entradaJugador(board, ficha):
    jugadaValida= False
    if ficha != "O":
        while not jugadaValida:
            entrada = int(input("Ingrese un numero del 1-9: "))-1
            if entrada > 9 or entrada < 0:
                print("Jugada no valida")
            elif board[entrada]=="-":
                board[entrada]= ficha
                jugadaValida = True
            else: print("La casilla esta ocupada elija otra")
    else:
        bot(board,ficha,jugadaValida)

def checkearWin(board):
    ganador = False
    slot = 0
    tamanio = len(board)
    while not ganador and slot < tamanio:
        if board[slot]==board[slot+1]==board[slot+2] and board[slot]!= "-" :
           ganador = True
        elif board[slot//3]==board[(slot//3)+3]==board[(slot//3)+6] and board[slot//3]!= "-" :
            ganador = True
        slot += 3
    if not ganador and  ((board[0]==board[4]==board[8] !="-" )or (board[2]==board[4]==board[6] !="-")):
        ganador = True
    return ganador

def bot(board,ficha,bool):
    while not bool:
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            bool = True

def jugar():
    jugadas=0
    board = generarBoard()
    ganador = False
    fichas = ["X", "O"]
    while jugadas != 9 and not ganador:
        entradaJugador(board, fichas[jugadas% 2])
        ganador = checkearWin(board)
        mostrarTablero(board)
        jugadas += 1
        if ganador:
            print("Felicitaciones ganaste ,jugador", fichas[jugadas % 2 - 1])
    if not ganador:
        print("Empate")
