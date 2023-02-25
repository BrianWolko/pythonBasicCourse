n1 = int(input("Primer numero: "))
n2 = int(input("segundo numero: "))

suma = n1 +n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2} la suma es {suma}
Para los numeros {n1} y {n2} la resta es {resta}
Para los numeros {n1} y {n2} la multiplicación es {multi}
Para los numeros {n1} y {n2} la división es {div}
"""
print(mensaje)