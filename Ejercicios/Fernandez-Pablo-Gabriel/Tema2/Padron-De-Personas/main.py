""" 
El archivo personas.csv contiene un padrón de personas a razón de una persona por línea y en
cada una separadas con comas el documento, nombre, apellido y edad. Desarrollar un programa
en python que lea el archivo y guarde todo su contenido en un diccionario indexado por
documento. Luego el programa debe ofrecer un menú con las siguientes opciones:
- Búsqueda por documento: que solicite un documento y si lo encuentra muestre todos los datos
  de la persona encontrada y un mensaje adecuado si no la encuentra.
- Búsqueda por apellido: que solicite un apellido y muestre por pantalla todos los datos de todas
  las personas cuyo apellido sea igual al ingresado.
- Mostrar el promedio de edades de todos. 
"""
import csv

def leer_archivo(arch):
    with open(arch, mode='r') as csv_arch:
        lector_csv = csv.DictReader(csv_arch, ['DNI', 'Nombre', 'Apellido', 'Edad'])
        """ cont_lineas = 0   #Esta parte muestra el contenido del archivo por consola
        for fila in lector_csv:
            if cont_lineas == 0:
                print(f'{", ".join(fila)}')
                cont_lineas += 1
            print(f"{fila['DNI']}, {fila['Nombre']}, {fila['Apellido']}, {fila['Edad']}")
            cont_lineas += 1
        print("Cantidad de filas del archivo:", cont_lineas) """
        return list(lector_csv)
        

def menu():
    print("Menu de opciones:\n" \
	"1) Busqueda por ducumento.\n" \
	"2) Busqueda por apellido.\n" \
	"3) Mostrar promedio de edades de todos.\n" \
	"4) Salir.")
    

def buscar_por_dni(dni, lector_csv):
    for fila in lector_csv:
        if dni == int(fila["DNI"]):
            return (f"DNI: {fila["DNI"]}, Nombre: {fila["Nombre"]}, Apellido: {fila["Apellido"]}, Edad: {fila["Edad"]}")
    return "No se ha encontrado a la persona..."


def buscar_por_apellido(ape, lector_csv):
    for fila in lector_csv:
        if ape.lower() == fila["Apellido"].lower():
            return (f"DNI: {fila["DNI"]}, Nombre: {fila["Nombre"]}, Apellido: {fila["Apellido"]}, Edad: {fila["Edad"]}")
    return "No se ha encontrado a la persona..."


def calcular_promedio_edades(lector_csv):
    cont = 0
    acu = 0

    for fila in lector_csv:
        cont += 1
        acu += int(fila["Edad"])

    return (acu // cont)

def main():
    arch = 'personas.csv'
    lector_csv = leer_archivo(arch)
    
    print("***PADRON DE PERSONAS***")
    menu()
    opt = int(input("Ingrese una opcion: "))
    
    while opt != 4:
        match opt:
            case 1:
                dni = int(input("Ingrese un nro de documento: "))
                cadena = buscar_por_dni(dni, lector_csv)
                print(cadena)
            case 2:
                ape = input("Ingrese un nro de documento: ")
                cadena = buscar_por_apellido(ape, lector_csv)
                print(cadena)
            case 3:
                prom = calcular_promedio_edades(lector_csv)
                print("El promedio de todas las edades es:", prom)
            case 4:
                break
            case _:
                print("ERROR! Ingrese una opcion valida...")
        input()
        menu()
        opt = int(input("Ingrese una opcion: "))
        
    print("Ha salido del programa...")
    

if __name__ == "__main__":
    main()