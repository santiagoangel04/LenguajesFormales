#conversion invalida
#print(dict(["q0","q1","q2"]))

transiciones = "q0,a->q0 q0,b->q1 q1,a->q1 q1,b->q2 q2,a->q1 q2,b->q1".split(" ")
#funciones
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

print(automata(transiciones))