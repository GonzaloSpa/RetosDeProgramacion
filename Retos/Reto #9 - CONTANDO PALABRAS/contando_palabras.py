# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */


def contar_palabras_iguales(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Inicializar un diccionario para almacenar los conteos
    conteos = {}

    for palabra in palabras: 
         # Convertir la palabra a minúsculas para evitar contar palabras con mayúsculas y minúsculas diferentes como distintas
        palabra = palabra.lower()

           # Actualizar el conteo de la palabra en el diccionario
        conteos[palabra] = conteos.get(palabra, 0) + 1

     # Filtrar el diccionario para mantener solo las palabras que se repiten
    palabras_repetidas = {palabra: conteo for palabra, conteo in conteos.items() if conteo > 1}
    
    return palabras_repetidas


# ejecucion 

string = "Hola hola holaa! como estas querido, como te trata el tiempo"
contando_repetidos = contar_palabras_iguales(string)
# print(f"La palabras repetidas son: {contando_repetidos}")

for palabra, conteo in contando_repetidos.items():
    print(f"{palabra}: {conteo}")