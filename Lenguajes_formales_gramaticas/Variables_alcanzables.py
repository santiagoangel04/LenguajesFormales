"""
Input Format

N, un entero de variables de la gramática en la primera línea

N líneas de Variable -> Producción|..|Producción|

donde Producción es cualquier cadena de VxE (variables o alfabeto) o lambda

Constraints

Este taller tiene la opción de hacerse en parejas. Se aceptan trabajos únicamente de parejas o individuales. Código compartido entre individuales o parejas de otros será considerado plagio.

Output Format

El conjunto de variables NO terminables en forma {V,..,Z}

Sample Input 0

7
S -> aS | AaB | ACS
A -> aS | AaB | AC
B -> bB | DB | BB
C -> aDa | ABD | ab
D -> aD | DD | ab
E -> FF | aa | aa
F -> aE | EF | EF
Sample Output 0

{E,F}
Explanation 0

Vease ejemplo 4.7.3 del libro

Sample Input 1

2
S -> a
A -> aA | lambda
Sample Output 1

{A}

"""


def creacion_gramatica():
    #numero de variables de la gramatica
    n = int(input())
    gramatica = dict()
    for i in range(n):
        variable,transiciones = input().split("->")
        gramatica[variable.replace(" ","")] = transiciones.replace(" ","").split("|")
    #print(gramatica)
    return gramatica,set(next(iter(gramatica))[0])

# por definicion S siempre sera una variable alacanzable
#la forma next(iter())->trae el primer elemento de mi gramatica, porque S siempre es alcanzable
def maquina_proceso_variable_alcanzable(*args):
    #parametros
    gramatica_creada:dict = args[0][0]
    #print(type(gramatica_creada))
    variable_alcanzable:set = args[0][1]
    #print(type(variable_alcanzable))
    def procesador_cadenas(cadena:str):
        for cadena_para_procesar in cadena:
            if cadena_para_procesar.isupper():
                variable_alcanzable.add(cadena_para_procesar)

    for variable,produccion in gramatica_creada.items():
        if variable in list(variable_alcanzable):
            for cadena_sin_procesar in produccion:
                procesador_cadenas(cadena_sin_procesar)
    return variable_alcanzable,gramatica_creada

def variables_alcanzables(*args):
    resultado = "{"
    variables_alcanzables_encontradas:set = args[0][0]
    gramatica:dict = args[0][1]
    for i in gramatica.keys():
        if i not in list(variables_alcanzables_encontradas):
            resultado += i+","
    resultado =resultado.rstrip(",")
    resultado+="}"
    return resultado
#print()
print(variables_alcanzables(maquina_proceso_variable_alcanzable(creacion_gramatica())))
