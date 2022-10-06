
def suma(n, m):
    """
    La función suma recibe dos números y
    retorna el resultado de la suma de ambos
    Args:
        n: El primer sumando
        m: El segundo sumando
    Returns::
        La suma de los argumentos
    suma :: int, int -> int
    """
    return n+m

def test_suma():
    assert suma(2,3) == 5
    assert suma(0,0) == 0
    assert suma(0,42) == 42


def resta(n,m):
    """
    La función resta recibe dos números y
    retorna el resultado de la resta del primero menos el segundo
    Args:
        n: El minuendo
        m: El sustraendo
    Returns::
        el resultado de la operación resta de minuendo menos el sustraendo
    resta :: int, int -> int
    """
    return n-m

def test_resta():
    assert resta(5,1) == 4
    assert resta(0,0) == 0
    assert resta(0,5) == -5

def multiplica(n,m):
    ...

def divide(n,m):
    ...

def tomar_opcion_del_menu():
    """
    La función muestra el menú y espera una opción por teclado.
    Args:
        No toma
    Returns:
        La opción elegida por el usuario
    """
    msg = """Seleccione una operación:
    1. Suma
    2. Resta
    3. Multiplica
    4. Divide
    5. Salir
"""
    opcion = input(msg)
    return opcion


def calculadora():
    """
    La función realiza diferentes operaciones aritméticas (suma, resta, multiplicación y división)
    entre dos números. La operación y operandos serán pedidos al usuario mediante el teclado.
    Esta función se llamará recursivamente hasta que el usuario elija la opción de salir del programa.
    Args:
        No tiene
    Returns:
        La función no tiene return explícito (devuelve None de manera implícita)
    """
    opcion = tomar_opcion_del_menu()
    if opcion not in ("1", "2", "3", "4"):
        print("Opción no válida. Mejor suerte la próxima")
        calculadora()
    else:
        n = int(input("Ingrese el primer operando: "))
        m = int(input("Ingrese el segundo operando: "))
        if opcion == "1":
            resultado = suma(n, m)
        elif opcion == "2":
            resultado = resta(n,m)
        elif opcion == "3":
            resultado = multiplica(n,m)
        elif opcion == "4":
            resultado = divide(n,m)
        elif opcion == "5":
            ...
        print(resultado)
        calculadora()
