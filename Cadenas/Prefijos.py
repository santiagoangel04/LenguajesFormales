#########PROBLEMA######
"""
Dada una cadena, se debe extraer todos los prefijos de dicha cadena. Por ejemplo, dado la cadena "java", todos los prefijos son:
java
jav
ja
j
Input Format
Hola,Mundo!
Constraints
la cadena no tendrá espacios
se imprime primero la cadena completa y luego los prefijos en orden descendente, una por línea
Output Format
Hola,Mundo!
Hola,Mundo
Hola,Mund
Hola,Mun
Hola,Mu
Hola,M
Hola,
Hola
Hol
Ho
H
Sample Input 0
Hola,Mundo!
Sample Output 0
Hola,Mundo!
Hola,Mundo
Hola,Mund
Hola,Mun
Hola,Mu
Hola,M
Hola,
Hola
Hol
Ho
h
"""
######ANALISIS#######
"""
Para este problema, podemos plantearnos la misma solucion de las subcadena,dado que el es consecuente a este problema, en el problema podemos notar que no se substraen caracteres de la derecha, si no solo de la izquierda es decir, para el codigo anterior teniamos cosas como ->(hell,hel,he,h,ello,ell,ell,el,e...etc), es decir la solucion es mas facil de lo que se esperaba, solo es necesario utilizar de nuevo los slicings, ya no necesitaremos el uso de la recursion, solo sera necesario un for
Para el caso de los sufijos es lo mismo, ya no quiero quitar letras a la derecha, para los sufijos quito los de la izquierda
"""
cadena = input()

for less_ca in range(len(cadena),0,-1):
    print(cadena[:less_ca])