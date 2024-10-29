def automata(transcisiones:list,estados:list)->dict:
    atomata_build = {i:[] for i in estados}
    for x in transcisiones:
        x = x.split(",")
        if x[0] in atomata_build:
            estado_Dict, transition_Dict= x[0], x[1].split("->")
            atomata_build[estado_Dict].append(transition_Dict)
    return atomata_build

def verificacion_cadena(estado_inicial:str,cadena:str,automata:dict,estados_aceptacion:list)->bool:
    dis_automata = automata
    for i in cadena:
        recorrido = dis_automata.get(estado_inicial)
        for j in recorrido:
            if j[0] == i:
                estado_inicial = j[1]
                break
    if estado_inicial in estados_aceptacion:
        print("ACEPTADA")
    else:
        print("RECHAZADA")



alfabeto = input().split(" ")
estados =input().split(" ") #["q0", "q1", "q2"]
estado_inicial = input()
estados_finales = input().split(" ")#["q0","q2"]
transciones = input().split(" ") #"q0,a->q0 q0,b->q1 q1,a->q1 q1,b->q2 q2,a->q1 q2,b->q1".split(" ")
num_cadenas = int(input())

for i in range(num_cadenas):
    cadena = input() #acepta
    verificacion_cadena(estado_inicial,cadena,automata(transciones,estados),estados_finales)