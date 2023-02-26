palabra = "ab fg ba"

def no_space(texto):
    nuevo_texto =""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def es_palindromo(texto):
    i = 0
    esPalindromo = True
    texto = no_space(texto).lower()
    j = len(texto)-1
    while i < j:
        if texto[i] != texto[j]:
            esPalindromo = False
            break
        else:
            i+=1
            j-=1
    return esPalindromo

print(palabra, es_palindromo(palabra))
