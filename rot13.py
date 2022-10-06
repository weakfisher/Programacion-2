def cifrar(s):
    """
    Devuelve un conjunto con todas las letras de un stri,ng

    Args:
        s : String

    Returns:
        return a char cifrado
    """
    chars = set()
    for c in s.lower():
        if ord(c) >= 97 and ord(c) <=122:
            c  = (ord(c) + 13) % 26
            chars.add(c)

    return chars

def hacer_string(set):
    for i in j:
        x = str(i)
        codificado.write(x)


entrada = input("Ingrese Archivo a cifrar ")
archivo = open(entrada, "r")
destino = input("Ingrese Archivo de destino ")
codificado = open(destino,"w+")
cifrados = set()
for i in archivo:
        linea = i.rstrip()
        separado =linea.split(" ")
        for i in separado:
            j = cifrar(i)
            hacer_string(j)


codificado.close()
