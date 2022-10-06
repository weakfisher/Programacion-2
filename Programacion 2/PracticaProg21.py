import random

#---------------RECETA PYTHON
def temperaturas():
	temp = float(input("Ingrese una temperatura: ?"))
	charr = input("Ingrese el tipo de temperatura(F | Fahrenheit - C | Celsius: ?")
	if (charr == "F"):
		temp_c = (temp-32)*5/9
		print(temp_c)
	elif (charr == "C"):
		temp_f = (temp*1.8)+32
		print(temp_f)
	else:
		print("Temperatura no valida")

def fmaximo(x,y):
	if x > y:
		return x
	else:
		return y

def test_fmaximo():
	assert fmaximo(3,4) == 4
	assert fmaximo(-4,92) == 92
	assert fmaximo(-10,2) == 2
	assert fmaximo(-5,72) == 72

#------------PRACTICA 4
#Ejercicio 1
#A
def primerosChar():
	string = input("Ingrese una palabra: ?")
	if string == "":
		return "Cadena vacia"
	else:
		substring = string[0]+string[1]
		return substring

#B
def ultimosChar():
	string = input("Ingrese una palabra: ?")
	if string == "":
		respuesta = "Cadena vacia"
	else:
		respuesta = string[-3]+string[-2]+string[-1]
	return respuesta

#C
def cadados():
	string = input("Ingrese una palabra: ?")
	if string == "":
		respuesta = "Cadena vacia"
	else:
		respuesta = string[::2]
	return respuesta

#D
def sentidoInverso():
	string = input("Ingrese una palabra: ?")
	if string == "":
		respuesta = "Cadena vacia"
	else:
		respuesta = string[::-1]
	return respuesta

#E
def sentidoEinverso():
	string = input("Ingrese una palabra: ?")
	if string == "":
		respuesta = "Cadena vacia"
	else:
		respuesta = string[::]+string[::-1]
	return respuesta

#Ejercicio 2
def contar(l,x):
	suma = 0
	if l in x:
		suma += 1
		respuesta = suma
	return respuesta

#Ejercicio 3?

#Ejercicio 4
def ej4(s):
    """
    diseno:
    palabra : string
    signatura:
    ej4 : string -> int
    proposito:
    recibe una cadena de palabras separadas por espacios
    y debvuelve cuantas palabras de mas de 5 letras contiene la cadena.
    ejemplos:
    ej4("hola como estas") = 0
    ej4("hola") = 0
    ej4 ("programacion programa") = 2
    """
    cant_letras = 0
    cant_palabras =0
    for caracter in s:
        if caracter.isspace():
            if cant_letras >5:
                cant_palabras += 1
            cant_letras = 0
        else:
            cant_letras +=1
    if cant_letras > 5:
        cant_palabras+=1
    print(cant_palabras)

def ej5(s):
    """
    recibe una cadena de caracteres y devuelve la primera letra
    de las palabras que contiene
    ej:
    ej5 ("redictado prog") = "rp"
    ej5 ("universidad nacional rosarina") = "unr"
    ej5 ("facultad ciencias exactas ingenieria agrimensura") = "fceia"
    """
    string = ""
    for i in range(len(s)):
        if i == 0:
            string += s[i]
        if s[i].isspace():
            string+=s[i+1]
    return string

def ej5b(s):
    """recibe un string y devuelve la primera letra de
    cada palabra en mayuscula
    ej:
    repulica argentina = RA
    universidad nacional rosario = UNR
    """
    return (ej5(s).upper())

def es_a(l):
    return (l == "A" or l == "a" or l == "Á" or l=="á")

def ej5c(s):
    """recibe un string y devuelve las palabras
    que comiencen con la letra a
    ejemplo:
    "antes de ayer almorce y cene" = "antes ayer almorce"
    "republica argentina" = "argentina"
    """
    string = ""
    strings_a = ""
    for caracter in s:
        if caracter.isspace():
            if es_a(string[0]):
                strings_a += string + " "
            string = ""
        else:
            string+=caracter
    if es_a(string[0]):
        strings_a += string
    print (strings_a)

def ej5d():
    """recibe un string y devuelve las palabras
    que comiencen con la letra a
    ejemplo:
    "antes de ayer almorce y cene" = "antes ayer almorce"
    "republica argentina" = "argentina"
    """

#----------------PRACTICA 5
def ejercicio1():
	for i in range(10,21):
		print(i)

def factorial(n):
	suma = 1
	for i in range(1,n+1):
		suma *= i
		print(suma)

def factorialRecursiva(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return n*factorialRecursiva(n-1)


def ejercicio2():
	m = int(input("Cuantos valores va a calcular: ?"))
	for i in range(0,m):
		num = int(input("Ingrese un numero a calcular su factorial: ?"))
		resultado = factorialRecursiva(num)
		print(resultado)

def far_cel(temp):
	temp_c = (temp-32)*5/9
	return temp_c

def ejercicio3():
	temperatura = 0
	for i in range(0,121,10):
		temperatura = far_cel(i)
		print(i, "|", temperatura)

def ejercicio4(cant,tasa,years):
	interes = cant*(1+(tasa/100))**years

#Sin funcion
def ejercicio5(n):
	suma = 0
	for i in range(1,n+1):
		suma+=i
		print(i,"-",suma)

#Con funcion
def ejercicio5b(n):
	for i in range(1,n+1):
		calc = (i*(i+1))/2
		print(i,"-",calc)

def ejercicio6():
	hay_mas = "Si"
	while hay_mas == "Si":
		n = int(input("Ingrese un numero positivo: ?"))
		if n > 0:
			print("Es positivo")
		else:
			print("Vuelva a ingresar el numero")

		hay_mas = input("Quiere ingresar otro numero? -")

def leerCentinela():
	return input("Ingrese un numero, para terminar ingrese *: ? ")

def ejercicio6b():
	centinela = leerCentinela()
	while centinela != "*":
		n = int(centinela)
		if n > 0:
			print("Es positivo")
		else:
			print("Vuelvo a ingresar el numero")

		centinela = leerCentinela()

def leerCentinela2():
	return input("Ingrese una nota, para terminar *: ? ")

def ejercicio7():
	centinela = leerCentinela2()
	sumaNotas = 0
	repeticion = 0
	prom = 1

	while centinela != "*":
		nota = int(centinela)
		sumaNotas += nota
		repeticion += 1
		prom = sumaNotas/repeticion

		centinela = leerCentinela2()

	print("El promedio de todas las notas es: ",prom)

def leerCentinela3():
	return input("Ingrese un numero, -1 para salir: ")

def ejercicio8():
	centinela = leerCentinela3()
	sumaNumeros = 0
	cantNumeros = 0
	prom = 1
	while centinela != "-1":
		num = int(centinela)
		sumaNumeros += num
		cantNumeros += 1
		prom = sumaNumeros/cantNumeros

		centinela = leerCentinela3()
	print("Se ingresaron: ",cantNumeros)
	print("La suma total de los numeros ingresados es: ", sumaNumeros)
	print("El promedio de los numeros es: ",prom)

def multiplo(n,m):
	return n%m == 0

#EJERCICIO 9 ?????????????????????
def ejercicio9(n1,n2):
	suma = 0
	cant = 0
	for i in range(n1,n2+1):
		if n1*contador < n2:
			cant += 1
		contador += 1
	return cantidad

def ejercicio9B(n1,n2):
	contador = 1
	cant = 0
	while (n1*contador) < n2:
		contador += 1
		cant += 1
	return cant

print(ejercicio9B(2,8))

#----
def es_primo(n):
	flag = False
	if n < 1:
		return flag
	elif n == 2:
		flag = True
		return flag
	else:
		for i in range(2,n):
			if n % i == 0:
				return flag
			else:
				flag = True
			return flag

def ejercicio10(n):
	for i in range(2,n+1):
		primos = es_primo(i)
		if es_primo(i):
			print(i)

def ejercicio11():
	contra = "HolaMundo123"
	cont = input("Ingrese una contraseña: ? ")
	while cont != contra:
		cont = input("Ingrese una contraseña: ? ")

def ejercicio11b():
	suma = 1
	contra = "HolaMundo123"
	cont = input("Ingrese una contraseña: ? ")
	while suma < 3:
		suma += 1
		if cont != contra:
			cont = input("Ingrese una contraseña: ? ")

def ejercicio11c():
	flag = False
	contra = "HolaMundo123"
	suma = 0
	cont = input("Ingrese una contraseña: ? ")
	while suma < 3:
		suma += 1
		if cont != contra:
			return flag
		flag = True
		return flag

#Ejercicio 12
def es_potencia_de_dos(n):
	flag = True
	if n < 1:
		flag = False
		return flag
	elif n <= 2:
		return flag

	i = 2
	while flag == True:
		i*=2
		if i == n:
			return flag
		elif i > n:
			flag = False
			return flag

def ejercicio12b(n,m):
	suma = 0
	for i in range(n,m):
		if es_potencia_de_dos(i):
			suma += i
	print(suma)

#-----------------------------PRACTICA 6-------------------
#Ejercicio 1
def lanzamientosDados():
	n = random.randint(1,6)
	while n != 6:
		n = random.randint(1,6)
		print(n)

#Ejercicio 2
def lanzamientosDadosDef():
	n = int(input("Ingrese cuantas veces quiere lanzar los dados: ? "))
	dado1 = random.randint(1,6)
	dado2 = random.randint(1,6)
	suma = 0
	contar = 0
	for i in range(1,n+1):
		dado1 = random.randint(1,6)
		dado2 = random.randint(1,6)
		print(dado1," | ",dado2)

		if (dado1 == dado2):
			suma += 1
	print("La cantidad de veces que los dados fueron iguales es: ",suma)

#Ejercicio 3
def centinelaDado():
	return input("Quiere lanzar nuevamente? <Si> <No>")

def lanzamientosDados3():
	centinela = centinelaDado()
	dado = random.randint(1,6)
	contador = 0
	resultadoFinal = 0
	while centinela != "No":
		centinela = input(centinela)
		dado = random.randint(1,6)

		centinela = centinelaDado()
