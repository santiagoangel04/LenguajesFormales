"""
N, un entero de variables de la gramática en la primera línea

N líneas de Variable -> Producción|..|Producción|

donde Producción es cualquier cadena de VxE (variables o alfabeto) o lambda

Constraints

Este taller tiene la opción de hacerse en parejas. Se aceptan trabajos únicamente de parejas o individuales. Código compartido entre individuales o parejas de otros será considerado plagio.

Output Format

El conjunto de variables NO terminables en forma {V,..,Z}

Sample Input 0

6
S -> ACD | bBd | ab
A -> aB | aA | C
B -> aDS | aB
C -> aCS | CB | CC
D -> bD | ba
E -> AB | aDb
Sample Output 0

{C}
Explanation 0

Véase ejemplo 4.7.2 del libro

Sample Input 1

2
S -> a | AB
A -> aA | lambda
Sample Output 1

{}
Explanation 1

No hay variables NO terminables
"""

def creacion_gramatica():
    #numero de variables de la gramatica
    n = int(input())
    gramatica = dict()
    gramatica_inicial=dict()
    for i in range(n):
        variable,transiciones = input().split("->")
        gramatica_inicial[variable.replace(" ","")] = transiciones.replace(" ","").split("|")
        gramatica[variable.replace(" ","")] = transiciones.replace(" ","").split("|")
    #print(gramatica)
    return gramatica,gramatica_inicial

#elimina las variables terminales y buscamos las variables en las producciones
def limpiando_gramatica(gramatica_limpia:dict,posibles_terminales_dict:dict):
    #funcion que remplaza variables por caracteres
    def helper_variable_cadena(cadena:str,elementos_cambio:dict):
        nueva_cadena = ""
        for caracter in cadena:
            if caracter in elementos_cambio.keys():
                for variable_terminal in elementos_cambio.keys():
                    if caracter == variable_terminal:
                        nueva_cadena+=elementos_cambio[variable_terminal]
            else:
                nueva_cadena+=caracter
        return nueva_cadena     
    def variable_cadena(gramatica_nueva:dict,variables_terminables_posibles:dict):
        for variable,produccion in gramatica_nueva.items():
            nueva_produccion = []
            for cadena in produccion:
                nueva_produccion.append(helper_variable_cadena(cadena,variables_terminables_posibles))
            gramatica_nueva[variable] = nueva_produccion

        return gramatica_nueva
        
    #busco la variable con sus producciones para eliminarlas
    #esta variable ya a sido clasificada como terminable
    for variable in posibles_terminales_dict.keys():
        try:
            if variable in gramatica_limpia.keys():
                del(gramatica_limpia[variable])
        except KeyError as e:
            return False
    return variable_cadena(gramatica_limpia,posibles_terminales_dict)

#hago una estructura anidada por mejora visual 
def buscador_terminables_gramatica(gramatica_creada:dict,posibles_terminables:dict):
    def buscador_helper_cadenas(cadena_produccion:str):
        tiene_variables = False
        cadena_ultima = ""
        for caracter in cadena_produccion:
            if caracter.isupper():
                tiene_variables = True
            else:
                cadena_ultima+=caracter
        return cadena_ultima,tiene_variables
    
    for variable,produccion in gramatica_creada.items():
        es_cadena_terminal = []
        for cadena in produccion:
            cadena_terminal_ultima,resultado_busqueda = buscador_helper_cadenas(cadena)
            es_cadena_terminal.append(resultado_busqueda)
        if False in es_cadena_terminal:
            posibles_terminables[variable] = cadena_terminal_ultima
    return posibles_terminables,limpiando_gramatica(gramatica_creada,posibles_terminables)     
    

def variable_terminable(gramatica:dict):
    gramatica_antigua = gramatica
    gramatica_nueva = {}
    terminales_acumulados = {}
    for i in range(len(gramatica)//2):
        terminales_acumulados,gramatica_nueva =buscador_terminables_gramatica(gramatica_creada=gramatica,posibles_terminables=terminales_acumulados)
    if len(gramatica_nueva) > 0:
        for letra,valor in gramatica_nueva.items():
            return"{"+letra+"}"
    elif len(gramatica_nueva) <= 0:
        return"{}"

