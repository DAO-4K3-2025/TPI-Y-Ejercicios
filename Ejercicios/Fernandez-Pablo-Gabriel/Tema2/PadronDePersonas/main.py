"""
# Padrón de personas
El archivo personas.csv contiene un padrón de personas a razón de una 
persona por línea y en cada una separadas con comas el documento, 
nombre, apellido y edad. Desarrollar un programa en python que lea 
el archivo y guarde todo su contenido en un diccionario indexado por 
documento. Luego el programa debe ofrecer un menú con las siguientes 
opciones:

- Búsqueda por documento: que solicite un documento y si lo encuentra 
muestre todos los datos de la persona encontrada y un mensaje 
adecuado si no la encuentra.
- Búsqueda por apellido: que solicite un apellido y muestre por 
pantalla todos los datos de todas las personas cuyo apellido sea 
igual al ingresado.
- Mostrar el promedio de edades de todos. 
"""
import csv


def leer_archivo(nombre):
    m = open(nombre, "r")




def main():
    nombre = "personas.csv"

    leer_archivo(nombre)


if __name__ == "__main__":
    main()
