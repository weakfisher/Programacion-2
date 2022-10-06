from random import *
def hasta20():
    for i in range(11,20):
        print(i)

#ejercicio 3
def hastaN(n):
    for i in range(0,n+1):
        print(i)
#ejercicio 4
def factorial():
    factorial = int(input("ingrese num "))
    for i in range (1,factorial):
        factorial= factorial * i
        print(factorial)


#ejercicio 5
 #farCel: Int -> Int
 #El parámetro representa una temperatura en Fahrenheit y,
 # se retorna su equivalente en Celsius.
 # entrada: 32, salida: 0
 # entrada: 212, salida: 100
 # entrada: -40, salida: -40
def farCel():
     for i in range(0,120,10):
         print((i-32)*5/9,i)
#ejercicio 6
    #Interes: Int Int Int -> Int
    #El 1° Parametro Representa cantidad de pesos
    #El 2° Parametro Representa tasa de Interes
    #El 3° Parametro Representa años
    # se retorna el monto final a obtener
def Inter(pesos,interes,años):
    for i in range(0,años+1):
        pesos*(1+interes/100)**años

#ejercicio 12b
#contraseñas
def contrasenas2():
    contra="hola"
    pregunta=input("Ingrese Contraseña: ")
    intentos = 1
    while intentos<2:
        intentos= intentos + 1
        if contra != pregunta:
            pregunta=input("Ingrese Contraseña: ")
        else:
            return "ingreso"


#ejercicio 12c
#contraseñas
def contrasenas():
    contra="hola"
    pregunta=input("Ingrese Contraseña: ")
    intentos = 0
    terminar=False
    while intentos<2:
        intentos= intentos + 1
        if contra != pregunta:
            return terminar
        terminar = True
        return terminar
    print("Ingreso")


#ejercicio 13
#esprimo: int ->int
def esprimo(n):
    red= False
    if n< 1:
        return red
    elif n == 2:
        red = True
        return red
    else:
        for i in range(2,n+1):
            if n % i == 0:
                return red
            else:
                red= True
            return red


def primo(n):

    for i in range(2,n+1):
        primo=esprimo(i)
        if esprimo(i):
            print(i)

#ejercicio 14
#potencia_dos: Natural -> boolean
def potencia_dos(n):
    red=True
    if n==2 or n==0 or n==1:
        return red
    else:
        i=2
        while red==True:
            i*=2
            if n==i:

                return red
            elif i>n:
                red= False
                return red

def suma_potencias(n,m):
    suma=0
    for i in range(n,m+1):
            if potencia_dos(i):
                suma+=i
    print(suma)

    ##PRACTICA 3
#el objetivo de cada ciclo es reducir el numero en 5 y sumarlo a un string para al llegar a 20 imprimirlo
def ejercicio1 (n = 100):
 h = ""
 while n >= 20:
     h += ""+ str(n)
     n -= 5
 return h
def test_ejercicio():
    assert ejercicio1(25)=="2520"
    assert ejercicio1(30)=="302520"
    assert ejercicio1(15)==""
    assert ejercicio1(35)=="35302520"

def ejercicio2 (a, b, c):
    n = 2
    suma = 0
    sumas = 0
    if a/b > 30:
        suma = a/c*b**3
        return suma
    if a/b <= 30:
         while n <= 30:
             sumas += n**2
             n += 2
         return sumas


#ejercicio random
#lanzamieno dados1
def lanzamientoDados():
    suma = 0
    d = randint(0,7)
    while d!=7:
        suma= suma+ 1
        d =randint(0,7)
        print(d,suma)

def lanzamientoPerso(x):
    dado1=randint(0,7)
    iguales=0
    dado2=randint(0,7)
    for i in range (0,x+1):
        dado1=randint(0,7)
        dado2=randint(0,7)
        print(dado1," | ", dado2)
        if dado1==dado2:
            iguales= iguales + 1
    print(iguales)
#lanzamiento Dados 3
def lanzamientoJuego(x):
    dado=randint(1,6)
    alcancia= 0
    for i in range (0,x+1):
        dado=randint(1,6)
        print(dado)
        if dado==6:
            alcancia= alcancia + 4
        elif dado==1:
            alcancia=alcancia + 1
        elif dado==2 or 4 or 5:
            alcancia-= 2
        else:
            pass
    print("Su balanze es de ",alcancia)
