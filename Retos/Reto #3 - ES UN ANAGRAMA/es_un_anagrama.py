### Escribe una función que reciba dos palabras (String) y retorne
### verdadero o falso (Bool) según sean o no anagramas.
### - Un Anagrama consiste en formar una palabra reordenando TODAS
###   las letras de otra palabra inicial.
### - NO hace falta comprobar que ambas palabras existan.
### - Dos palabras exactamente iguales no son anagrama. 


def son_anagramas(palabra1, palabra2):
    # remplazo espacios y paso a minuscula ambas palabras
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # validamos si ambas palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False # en el caso de que no devolvemos False
    
    #r recorremos y con el metodo count() validamos si hay coincidencia en las letras 
    for letra in palabra1: 
        if palabra1.count(letra) != palabra2.count(letra):
            return False #en el caso de que no devuelvo False
    
    # si pasamos las validaciones son anagramas, devolvemos True
    return True


print(son_anagramas("listen", "silent"))  # Devuelve True
print(son_anagramas("hello", "world"))    # Devuelve False
    

   
  
        
        




