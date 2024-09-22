#diseñar una afd
def automata(transcisiones:list)->dict:
    atomata_build = dict()
    for i in transcisiones:
        element = i.split(",")
        #cambie la forma de interpretacion para la maquina
        """
        cambie -> por una lista esto necesario para el procesamiento del programa
        """
        atomata_build[element[0]] = element[1].split("->")
    return atomata_build


#primera linea alfabeto con split
alfabeto = input("Ingrese el alfabeto: ").split(" ")
#cantidad de estados que tiene el automata
estados = input("Ingrese los estados: ").split(" ")
#el primer estado del cual se formara el automata
estado_inicial = input("Ingrese el estado inicial: ")
#Estados finales
estados_finales = input("Ingrese los estados finales: ").split(" ")
#trancisiones 
transiciones = input("Ingrese todas las transciones: ").split(" ")
#numero cadenas que recibira el programa
num_cadenas = int(input("Ingrese el numero total de cadenas a evaluar: "))
#pedir cadenas
#comienzo del afd

print("Alfabeto:", alfabeto)
print("Estados:", estados)
print("Estado inicial:", estado_inicial)
print("Estados finales:", estados_finales)
print("Transiciones:", transiciones)
print("Número de cadenas:", num_cadenas)