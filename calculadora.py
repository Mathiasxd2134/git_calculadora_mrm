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

def main():
    print("Calculadora avanzada:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz logaritmo")

    opcion = int(input("Elige una operación (1/2/3/4/5/6/7):"))
    a = float(input("Ingresa el primer número: "))
    b = None
    if opcion in [1, 2, 3, 4, 5]:
        b = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print("Resultado:", suma(a, b))
    elif opcion == 2:
        print("Resultado de la resta es:", resta(a, b))
    elif opcion == 3:
        print("Resultado:", multiplicacion(a, b))
    elif opcion == 4:
        print("Resultado:", division(a, b))
    elif opcion == 5:
        print("Resultado:", potencia(a, b))
    elif opcion == 6:
        print("Resultado:", raiz_cuadrada(a))
    elif opcion == 7:
        print("Resultado:", logaritmo(a))
    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()

