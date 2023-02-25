edad = int(input("Ingrese edad:"))

# def checkearEdad(edad):
#     if edad > 54:
#         mensaje = "Puede ver la pelicula con descuento"
#     elif edad > 17:
#         mensaje = "Puede ver la pelicula"
#     else:
#         mensaje = "No puede ver la pelicula"

mensaje = "Es mayor" if edad > 17 else "es menor"

print(mensaje)

gas = False
encendido =True

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")