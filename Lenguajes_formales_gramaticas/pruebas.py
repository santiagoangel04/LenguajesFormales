import Variables_terminables as v_t
class VariablesInutules:
    def __init__(self):
        self.gramatica = dict()
        self.gramatica_sin_inutiles = ""

    def creacion_gramatica(self):
        n = int(input())
        for i in range(n):
            variable,transiciones = input().split("->")
            self.gramatica[variable.replace(" ","")] = transiciones.replace(" ","").split("|")

objeto = VariablesInutules()
objeto.creacion_gramatica()


v_t.variable_terminable(objeto.gramatica)
print(objeto.gramatica)
print(v_t.creacion_gramatica()[1])
