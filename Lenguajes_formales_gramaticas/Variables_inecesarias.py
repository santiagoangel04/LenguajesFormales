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
#se puede cambiar a clases pero esta algo largo
#variables alcanzables
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


############################################################################################

#variables terminables
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
    gramatica_nueva = {}
    terminales_acumulados = {}
    for i in range(len(gramatica)//2):
        terminales_acumulados,gramatica_nueva =buscador_terminables_gramatica(gramatica_creada=gramatica,posibles_terminables=terminales_acumulados)
   
    if len(gramatica_nueva) > 0:
        for letra,valor in gramatica_nueva.items():
            return"{"+letra+"}"
    elif len(gramatica_nueva) <= 0:
        return"{}"

#variable inutil
def variables_inutiles(var_alcansables:str,var_terminable:str,vieja:dict): 
    variables_inutiles_set = {var_alcansables[i] for i in range(len(var_alcansables)) if i % 2 !=0}
    variables_inutiles_set.update({var_terminable[i] for i in range(len(var_terminable)) if i % 2 !=0})
     

    #ahora imprimimos g
    resultantes = set(vieja.keys()).difference(variables_inutiles_set)
    gramatica_nueva_sin_inutiles = ""
    
    for variable,producciones in vieja.items():
        producciones_validas = []
        for i in producciones:
            if i != 'ACC':
                producciones_validas.append(i)
        if variable in resultantes:
            producc_var = ' | '.join(producciones_validas)
            gramatica_nueva_sin_inutiles += f"{variable} -> {producc_var}\n"
    
    return gramatica_nueva_sin_inutiles

if __name__ == "__main__":
    gramatica,vieja = creacion_gramatica()
    var_alc=variables_alcanzables(maquina_proceso_variable_alcanzable((gramatica,set(next(iter(gramatica))))))
    var_t=variable_terminable(gramatica)
    print(variables_inutiles(var_alc,var_t,vieja))
    