####DOCUMENTACION######
"""
Nota: Se que la programacion es un mundo de retos complicados, pero para este ejercicio decidi python por su facilidad y porque soy algo mas diestro
con este lenguaje, por eso no escogi los otros dos lenguajes

Analisis
Para este problema en particular se me solicitaba diseñar un algoritmo que me generara todas las subcadenas dado una cadena de longitud n, que no decia eso
pero era importante para mi analisis posterior, primeramente decidi crear una lista (despues me di cuenta que era inutil) que guardara cada una de las cadenas 
resultantes, lo dificil o no para el momento era determinar como sacar esas subcadenas. En python existe una forma de acceder a la cantidad de datos de una lista, como se sabe una string es una lista de caracteres, por ende el metodo se acomodaria bien, el metodo es el slicing(rebanar) que me permite acceder desde un elemento inicial a uno final o puede tener diferentes utilidades, un ejemplo seria de esta lista a=[1,2,3,4] extraer el elemento 2 3 y 4 sin la necesidad 
de un for, entonces sabemos que el 2 es el elemento de indice 1 y que el 4 es el ultimo elemento, su extraccion con slicing se puede hacer de varias formas 
1. a[1:]
2. a[1:4]
De esta manera fue que me parecio mas sencillo extraer las subcadenas, pero para este problema surgia otro problemas, la iteracion, como debia funcionar que cada vez que terminara una subcadena se quitara un caracter a la izquierda(hello->ello), para esto lo pense con for, con dos for, pero despues de unas pruebas 
y de analisar el problema mejor pense hacerlo con recursion. Para esta recursion debia tener dos cosas en cuenta, que no se fuera a visitar el infinito, y lo otro era que lo que hiciera funcionaba. Pude observar patrones en las subcadenas 
####Patrones#####
>>> cadena = "hello"
>>> cadena[0:5] 
'hello'
>>> cadena[0:4] 
'hell'
>>> cadena[:3] 
'hel' ...Etc
Para las otras subcadenas tenia lo siguiente
>>> cadena[1:5] 
'ello'
>>> cadena[1:4] 
'ell'
>>> cadena[1:3] 
'el'
>>> cadena[1:2] 
'e'
->Aqui existen casos interesantes que me llevo tiempo toma en cuenta
>>> cadena[1:1] 
''
>>> cadena[0:0] 
''
Los numeros llamemosle a y b deben ser diferentes en +1 si tengo 0 el otro numero debera ser 0+1=1 si tengo 1 entonces debe ser 1+1=1, si no corregia esto, el codigo tendria bugs, por eso se me ocurrio trabajar sobre cadenas modificadas, es decir apenas llegara a esta iteracion cadena[0:1] tenia que igualar la cadena original a este resultado pero quitandole un caracter a la izquierda.
Cada vez que este se guardara seria la cadena resultante que empezaba en 1 

####Codigo V.1
cadena = input()
sigma_estrella = list()
def creator_substring(cadena):
    if 1 == len(cadena) or len(cadena) == 0:#verifica que la cadena resultante este vacia o almenos tenga un elemento
        if len(cadena) == 1:
            sigma_estrella.append(cadena)#agrega elementos a la lista
        return #sale del bucle de la recursion
    else:
        for i in range(len(cadena),0,-1):
            sigma_estrella.append(cadena[:i])#slicing que estrae las subcadenas 
        cadena=cadena[1:] #modificacion de la cadena para que la resultanten sea la original -1 a su izquierda
        creator_substring(cadena) #recursion
creator_substring(cadena)
for element in sigma_estrella:#imprime las cadenas
    print(element)
"""
###codigo version 2
cadena = input()
def creator_substring(cadena):
    if 1 == len(cadena) or len(cadena) == 0:#verifica que la cadena resultante este vacia o almenos tenga un elemento
        if len(cadena) == 1:
            print(cadena)#agrega elementos a la lista
        return #sale del bucle de la recursion
    else:
        for i in range(len(cadena),0,-1):
            print(cadena[:i])#slicing que estrae las subcadenas 
        cadena=cadena[1:] #modificacion de la cadena para que la resultanten sea la original -1 a su izquierda
        creator_substring(cadena) #recursion
creator_substring(cadena)
