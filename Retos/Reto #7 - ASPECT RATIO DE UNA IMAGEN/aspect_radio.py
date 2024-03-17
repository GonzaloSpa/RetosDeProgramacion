from PIL import Image
import requests
from io import BytesIO
# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo:
#  *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */
# creando la funcion para saber el aspect ratio de una imagen

def obtener_aspect_ratio(url):
    response = requests.get(url)
      # Abre la imagen con Pillow
    if response.status_code == 200:
        imagen = Image.open(BytesIO(response.content))
        # Obtiene las dimensiones de la imagen
        ancho, altura = imagen.size
        # Calcula el aspect ratio
        aspect_ratio = ancho / altura
        return aspect_ratio
    else:
        # Si la solicitud falla, imprime un mensaje de error
        print("Error al descargar la imagen. Código de estado:", response.status_code)
        return None
    
    
# ejecutamos unas pruebas 

imagen = "https://www.dacast.com/static/4db438d5ab4014fe896308b8fda33f21/what-is-video-aspect-ratio.png"
aspect_image = obtener_aspect_ratio(imagen)
print(f"el aspecto de la imagen es: {aspect_image}")
