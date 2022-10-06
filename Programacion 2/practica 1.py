from math import *
#ejercicio1
def pares25(contador):
    if contador <= 0:
        pares25(int(input("ingresar num valido")))
    else:
        if contador < 25:
            print(contador*2)
            pares25(contador+1)
        else:
            return

#ejercicio2
def pares100(contador):
    if contador <= 0:
        pares100(int(input("ingresar num valido")))
    else:
        if contador <= 100:
            print(contador*2 , contador)

            pares100(contador+1)
        else:
            return

#ejercicio 3
def paresN(contador, n):
    if contador <= 0:
        paresN(int(input("ingresar num valido")), n)
    else:
        if contador < n:
            print(contador*2, contador)
            paresN(contador+1, n)
        else:
            return

#ejercicio4
def paresMayoresQue(n,m):
    if m< n:
        print(m*2, m)
        paresMayoresQue(n-1,m-n+1)
    else:
        return
        #terminar

#ejercicio 5
def sumatoria50(n):
    if n<=50:
         return n + sumatoria50(n+1)
    else:
        return 0

#ejercicio6
def sumatoriaN(n, m):
    if n<=m:
        return n + sumatoriaN(n+1,m)
    else:
        return 0

#ejercicio7
def sumatoriaMayor(min,max,l):
    if l<=max and l>=min:
        return l + sumatoriaMayor(min,max,l+1)
    else:
        return 0

#ejercicio 7 /1.2
def duplica(name):
    return name*2

#ejercicio8
def duplicaN(name,n):
    return name*n

#ejercicio 9a
def suma(n,m):
    return n+m

def test_suma():
    assert suma(2,3) == 5
    assert suma(-1,0) == -1
    assert suma(0,0) == 0

#ejercicio9b
def resta(n,m):
    return n-m

def test_resta():
    assert resta(3,5) == -2

#ejercicio9c
def multiplica(n,m):
    return n*m

def test_multiplica():
    assert multiplica(2,1) == 2

#ejercicio 9d
def dividir(n,m):
    return n//m

#ejercicio 9e
def opciones_menu():
    msj= " 1 Multiplicar \n 2 Sumar \n 3 Resta \n 4 Diviri \n 5 Quit \n"

    opcion= input(msj)
    return opcion

def Calcu():
    opcion= opciones_menu()
    if opcion not in ("1","2","3","4","5"):
        print("ingresar valor correcto")
        Calcu()
    else:
        if opcion == "5":
            return
        else:
            n= int(input("Ingrese 1° Operando: "))
            m= int(input("Ingrese 2° Operando: "))
            if opcion == "1":
                 resultado = multiplica(n,m)
            elif opcion =="2":
                 resultado = suma(n,m)
            elif opcion == "3":
                 resultado = resta(n,m)
            elif opcion == "4":
                resultado = dividir(n,m)
        print(resultado)
        Calcu()
