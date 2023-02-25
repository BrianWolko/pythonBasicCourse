def suma(*numeros):
    resultado =0
    for numero in numeros:
        resultado += numero
    return resultado

print(str(suma(3, 3, 3, 3, 3, 3, 3)))