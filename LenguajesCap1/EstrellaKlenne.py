#####CREACION ALFABETO######

"""
Para este programa se nos planteaba crear el alfabeto de todas las cadenas de 
palabras que se crearan dado un conjnto de simbolos inicial, dividimos la entrada inicial
"""

alfabeto = input().split(" ")
sucesiones = int(input())


def generated_language(alfabeto:list,iter:int):
    aux = alfabeto.copy()
    cadena = ""
    total_cadenas = sum([len(alfabeto)**x for x in range(1,iter+1)])
    for i in aux:
        if len(aux) == total_cadenas:
            break
        else:
            for j in range(len(alfabeto)):
                cadena += i+alfabeto[j]
                aux.append(cadena)
                cadena = ""
    return aux

for i in generated_language(alfabeto,sucesiones):
    print(i, end = " ")