from random import *
def multiplo(n,m):
    if n%m == 0:
    	return 0
    else:
        return 1
a=[1,2,1,4,1,6,7]
def elimina(lista):
    print(lista[1:-1])
#ejercicio 1
def posicionesMultiplo(lista,n):
    resultad = lista[::n]
    return resultad
#ejercicio 2
def masSuma(listan):
    resultado = 0
    nuevalis = []
    for i in listan:
        resultado += i
        nuevalis.append(resultado)
    print (nuevalis)

#ejercicio 5
def duplicado(lista):
    duplicado = False
    longitud= len(lista)
    index = 0
    while index < longitud and (not(duplicado)) :
        elemento= lista[index]
        if lista.count(elemento) > 1:
            duplicado = True
        index = index + 1
    return duplicado

def eliminaDuplicado(lista):
    duplicado = False
    longitud= len(lista)
    index = 0
    listaNueva = []
    while index < longitud :
        elemento= lista[index]
        if lista.count(elemento) > 1:
            pass
        else:
            listaNueva.append(elemento)
        index = index + 1
    print(listaNueva)

def eliminaDuplicado2(lista):
    for i in lista[:]:
        if lista.count(i)>1:
            aux = 0
            while lista.count(i)> aux :
                lista.remove(i)
                aux += 1
    return lista
b=[1,2,3,4,4,4,5,6]
def prueba_eliminardups():
    assert(eliminaDuplicado2(a)==[2,4,1,6,7])
    assert(eliminaDuplicado2(b)==[1,2,3,4,5,6])

def elementosDistintos(lista):
    print(len(eliminaDuplicado2(lista)))

#def busquedaDicotomica(lista):

#ejericio Cadenas /    2
def contar(l,x):
    contador=0
    for i in l[:]:
        if x == i:
            contador += 1
    print(contador)
