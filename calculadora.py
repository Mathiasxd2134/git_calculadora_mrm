import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de número negativo."
    return math.sqrt(a)

def logaritmo(a):
    if a <= 0:
        return "Error: Entrada no válida para logaritmo."
    return math.log(a)


