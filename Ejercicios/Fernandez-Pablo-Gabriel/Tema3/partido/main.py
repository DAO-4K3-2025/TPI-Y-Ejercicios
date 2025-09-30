""" Un partido de fútbol se juega entre dos equipos denominados local y visitante. Desarrollar una clase Partido que
contenga referencias a dos objetos de la clase Equipo. La clase Partido debe poseer atributos para registrar ademas la
cantidad de goles realizada por cada equipo y métodos para informar cuál es el ganador o si hubo empate. Por otro
lado, la clase Equipo debe poseer un método RegistrarPartido que reciba por parámetro un partido y asigne atributos
(almacenados o calculados) para informar: 

Cantidad de partidos jugados
Cantidad de partidos jugados como local
Cantidad de partidos jugados como visitante
Suma de goles realizados
Suma de goles recibidos
Diferencia total de goles
Cantidad de partidos ganados
Cantidad de partidos empatados
Cantidad de partidos recibidos
Sumatoria de puntos (suponiendo que todos los partidos son de un mismo campeonato) """

from equipo import Equipo
from partido import Partido

def main():
    e1 = Equipo("Boca")
    e2 = Equipo("River")
    e3 = Equipo("Platense")

    p1 = Partido(e1, e2, 4, 2)
    p2 = Partido(e2, e1, 3, 4)
    p3 = Partido(e1, e3, 5, 0)
    p4 = Partido(e2, e3, 3, 1)
    p5 = Partido(e3, e1, 2, 2)
    p6 = Partido(e3, e2, 1, 1)
    """ print(e1)
    print(e2)
    print(e3) """

    #lista = [p1, p2, p3, p4]

    
    print(e1)
    print("---------------------------------------")
    #Cantidad de partidos jugados
    print(f"Partidos jugados: {e1.contar_partidos()}")

    #Cantidad de partidos jugados como local
    print(f"Partidos jugados como local: {e1.contar_partidos_local()}")

    #Cantidad de partidos jugados como visitante
    print(f"Partidos jugados como visitante: {e1.contar_partidos_visitante()}")

    #Suma de goles realizados
    print(f"Suma de goles realizados: {e1.goles_realizados()}")

    #Suma de goles recibidos
    print(f"Suma de goles recibidos: {e1.goles_recibidos()}")

    #Diferencia total de goles
    print(f"Diferencia total de goles: {e1.diferencia_goles()}")

    #Cantidad de partidos ganados
    print(f"Partidos ganados: {e1.partidos_ganados()}")

    #Cantidad de partidos empatados
    print(f"Partidos empatados: {e1.partidos_empatados()}")
    
    #Cantidad de partidos recibidos - Perdidos supongo
    partidosRecibidos = e1.contar_partidos() - (e1.partidos_ganados() + e1.partidos_empatados())
    print(f"Partidos recibidos: {partidosRecibidos}")


if __name__ == "__main__":
    main()