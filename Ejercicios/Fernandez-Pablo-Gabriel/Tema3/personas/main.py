""" Programar una clase Persona con atributos suficientes para almacenar documento, nombre,
apellido y edad de una persona. 

Crear un programa que permita ingresar los
datos de algunas personas por teclado y con esos datos cree instancias 
sin guardarlas en una estructura de datos y muestre por pantalla el estado de las mismas.

Al finalizar la carga el programa debe mostrar los datos de la persona de menor edad. """

from persona import Persona


def cargar_datos_persona():
    doc = input("Igrese el documento: ")
    try:
        doc_valido = int(doc)
    except ValueError:
        doc_valido = 0
    nom = input("Igrese el nombre: ")
    ape = input("Igrese el apellido: ")
    edad = input("Igrese la edad: ")
    try:
        edad_valida = int(edad)
    except ValueError:
        edad_valida = 18

    return Persona(doc_valido, nom, ape, edad_valida)


def main():
    print("*** PERSONAS ***")
    cant = int(input("- Ingrese la cantidad de personas a cargar: "))
    listPersonas = []

    for i in range(cant):
        print(f'Ingrese los datos de la persona {i+1}: ')
        per = cargar_datos_persona()
        listPersonas.append(per)

    primerVuelta = True
    menorEdadPersona = None
    for persona in listPersonas:
        if primerVuelta:
            menorEdadPersona = persona
            primerVuelta = False
            continue
        
        if not menorEdadPersona.__lt__(persona):
            menorEdadPersona = persona
    
    print("\n- La persona de menor edad es:")
    print(menorEdadPersona)


        





if __name__ == '__main__':
    main()