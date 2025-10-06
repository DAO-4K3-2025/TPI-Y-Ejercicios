""" # Biblioteca.py
    • Tipo de material (1 = libro físico, 2 = e-book, 3 = revista)
    • Código
    • Título
    • Autor
    • Precio base
    • Característica extra (días prestados, valor de venta, nacional/importada)

## Funcionalidades:

    1. Cargar materiales desde el archivo.
    2. Calcular el promedio entero de los precios base de todos.
    3. Obtener el material con mayor costo de mantenimiento.
    4. Calcular la suma de costo de mantenimiento de todos los préstamos.
    5. Contar cuántos libros físicos se prestaron por más de 30 días.
    6. Contar cuántas revistas son importadas.
    7. Calcular en un diccionario la cantidad de materiales de cada tipo, las 
    claves del diccionario deben ser "Libro", "Ebook" y "Revista". """
import csv
from material import Material
from libro import Libro
from ebook import Ebook
from revista import Revista

class Biblioteca:
    def __init__(self, archivo):
        self.materiales = []
        self.cargar_materiales(archivo)

    # 1. Cargar materiales desde el archivo.
    def cargar_materiales(self, archivo):
        with open(archivo, "r") as file:
            reader = list(csv.reader(file))
            for fila in reader:
                self.materiales.append(self.inicializar_material(fila))

    def inicializar_material(self, fila):
        if fila[0] == "1":
            return Libro(fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
        elif fila[0] == "2":
            return Ebook(fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
        else:
            return Revista(fila[1], fila[2], fila[3], int(fila[4]), fila[5])
    
    def cantidad_materiales(self):
        return self.materiales
    
    # 2. Calcular el promedio entero de los precios base de todos.
    def calcular_promedio_precios_base(self):
        total = sum(material.precio_base for material in self.materiales)
        return total // len(self.materiales)
    
    # 3. Obtener el material con mayor costo de mantenimiento.
    def obtener_material_mayor_costo_mantenimiento(self):
        max = 0
        material_max = None
        bandera = True
        for material in self.materiales:
            costo = material.calcular_costo_mantenimiento()
            if bandera or costo > max:
                max = costo
                material_max = material
                bandera = False
        return material_max

    # 4. Calcular la suma de costo de mantenimiento de todos los préstamos.
    def calcular_suma_costo_mantenimiento(self):
        return sum(material.calcular_costo_mantenimiento() for material in self.materiales)
    
    # 5. Contar cuántos libros físicos se prestaron por más de 30 días.
    def contar_libros_mas_30_dias(self):
        return sum(1 for material in self.materiales if isinstance(material, Libro) and material.dias_prestados > 30)

    # 6. Contar cuántas revistas son importadas.
    def contar_revistas_importadas(self):
        return sum(1 for material in self.materiales if isinstance(material, Revista) and material.origen == "importada")

    # 7. Calcular en un diccionario la cantidad de materiales de cada tipo, las 
    # claves del diccionario deben ser "Libro", "Ebook" y "Revista".
    def cantidad_por_tipo(self):
        conteo = {"Libro": 0, "Ebook": 0, "Revista": 0}
        for material in self.materiales:
            if material.tipo == 1:
                conteo["Libro"] += 1
            elif material.tipo == 2:
                conteo["Ebook"] += 1
            elif material.tipo == 3:
                conteo["Revista"] += 1
        return conteo
    


def main():
    b = Biblioteca("material.csv")
    print("Cantidad por tipo:", b.cantidad_por_tipo())

if __name__ == "__main__":
    main()

