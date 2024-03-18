# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

# utilizando recursividad 
def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else: 
        # concatenando el ultimo caracter de la cadena a la subcadena, sin el ultimo caracter 
        return cadena[-1] + invertir_cadena(cadena[:-1])

# ejecucion 

nueva_cadena = "Hola mundo"
cadena_invertida = invertir_cadena(nueva_cadena)
print(f"La cadena original es: {nueva_cadena}")
print(f"La cadena invertida es: {cadena_invertida}")