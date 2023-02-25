def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def programa(op = ""):
    while op.lower() != "salir":
        op = input("ingrese la operación a realizar: ")
        if op.lower() == "salir":
            break
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("ingrese el segundo número: "))
        match op:
            case '+':
                print(suma(n1,n2))
            case '-':
                print(resta(n1,n2))
            case '*':
                print(multiplicacion(n1,n2))
            case '/':
                print(division(n1,n2))
            case _:
                print("por favor ingrese dos números y un operador")

programa()
            