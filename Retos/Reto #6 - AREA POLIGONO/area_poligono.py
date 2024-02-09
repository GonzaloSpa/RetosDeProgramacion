import math
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */



class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


def calcular_y_mostrar_area(poligono):
    area = poligono.calcular_area()
    nombre_poligono = type(poligono).__name__  # Obtener el nombre de la clase del polígono
    print(f"Área del {nombre_poligono}: {area}")
    return area


# Ejemplos de uso:
triangulo = Triangulo(base=5, altura=8)
cuadrado = Cuadrado(lado=4)
rectangulo = Rectangulo(base=6, altura=9)

area_triangulo = calcular_y_mostrar_area(triangulo)
area_cuadrado = calcular_y_mostrar_area(cuadrado)
area_rectangulo = calcular_y_mostrar_area(rectangulo)

        
        