palabra = "abasba"

def es_palindromo(texto):
    i = 0
    j = len(texto)-1
    esPalindromo = True
    while i < j:
        if texto[i] != texto[j]:
            esPalindromo = False
            break
        else:
            i+=1
            j-=1
    return esPalindromo

print(palabra, es_palindromo(palabra))
