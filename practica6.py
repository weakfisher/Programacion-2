#desordenada : list elemento
#devuelve la cantidad de veces que aprece el elemento ingresado en la lista dada
#busque la primera vez que aparece y devuelva su index
#devuelve las posiciones en las que se encuentran dichos elementoss

a = [1,2,3,1,41,1,52,11,2,11,1]
b = ["galopar","galpon","galpear","perno","galopar","galopo"]
def desordenda(list,elemento):
    contador = 0
    listaPos = []
    index = 0
    for i in range (0, len(list)):
        if list[i]==elemento:
            index= list.index(elemento)+1
            listaPos.append(i+1)
            contador += 1

    print(elemento,"aparece", contador, "veces. Aparece por primera vez en la posicion ",index, ".Dicho elemento aparece en las posiciones", listaPos)
#maxim list -> int tupla
def maxim(list):
     maximo =  max(list)
     lugarmax = (list.index(maximo)+1, maximo)
     print (maximo," | ",lugarmax)

#lugarBinario: list element -> list
#verifica si el elemento se encuentra en la lista, si es asi
#encuentra su posicion mediante busqeuda binaria
#en caso contrario lo agrega a su posicion correspondiente y devuelve tal posicion
#todo esto en una lista ordenada
c = [1,2,4,5,6,7,8,9,10,11,15,16]
def binary_search(l, x):
    first = 0
    end = len(l) - 1
    indice = -1 # encontrado = False

    while (first <= end and indice == -1): # and not encontrado
        m = (first + end) // 2
        if l[m] < x:
            first = m + 1
        elif l[m] > x:
            end = m - 1
        else:
            indice = m # encontrado = True

    return indice # return encontrado

def lugarBinario(list, elemento):
    listaOrdenada= []
    if elemento in list:
        listaOrdenada = binary_search(list,elemento)
        print ("Se encuentra en la posicion",listaOrdenada+1)
    else:
        listaOrdenada= list
        listaOrdenada.insert(elemento-1,elemento)

        return listaOrdenada
        print (listaOrdenada)


## PRACTICA DICCIONARIO
#ejercicio 1
# transADic : list -> dictionary
l =[ ("Hola", "don Pepito"), ("Hola", "don Jose"),("Buenos", "días")]
j ={ ("Hola", "don Pepito"), ("Hola", "don Jose"),("Buenos", "días")}
def trasnADic(tupla):
    c = {}
    b = []
    for x, y in tupla:
        if not x in c:
            c[x] = y
        else:
            if y not in b:
                b.append(y)
            c[x]  +=  b

    print(c)


def crearLista(lista):
    c = []

    for i in lista.keys():
        p=[]
        p.append(i)
        for j in lista:
            if(j[0]==i):
                p.append(j[1])
        return p
#falta poner las claves en una lista

#ejercicio 2 diccionario
def contarAP(cadena):
    a = cadena.split()
    contador
    for i in a:
        pass
