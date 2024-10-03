def suma(a, b):
    c = a + b
    print("La suma de ", a, " y ", b, " es: ", c)

def resta(a, b):
    c = a - b
    print("La resta de ", a, " y ", b, " es: ", c)

def multiplicacion(a, b):
    c = a * b
    print("La multiplicacion de ", a , " y ", b, " es: ", c)

def divicion(a, b):
    if (a != 0 and b != 0):
        c = a / b
        print("La divicion de ", a, " y ", b, " es: ", c)
    else:
        print("No se puede dividir por 0")

def resto(a, b):
    if (a != 0 and b != 0):
        c = a % b
        print("El resto de ", a, " y ", b, " es: ", c)
    else:
        print("No se puede dividir por 0")



def divicionReal(a, b):
    if (a != 0 and b != 0):
        c = a // b
        print("La divicion real de ", a, " y ", b, " es: ", c)
    else:
        print("No se puede dividir por 0")

def potencia(a, b):
    c = a ** b
    print("La potencia de ", a, " al ", b, " es: ", c)

