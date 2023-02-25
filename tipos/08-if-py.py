edad = int(input("Ingrese edad:"))

def checkearEdad(edad):
    if edad > 54:
        print("Puede ver la pelicula con descuento")
    elif edad > 17:
        print("Puede ver la pelicula")
    else:
        print("No puede ver la pelicula")

checkearEdad(edad)