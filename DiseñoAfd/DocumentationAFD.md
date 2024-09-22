# Creacion AFD
## Problema
Crea un programa para simular un autómata finita determinista. La máquina es una tupla de alfabeto, estados, estado inicial, estados finales y transiciones. El programa leerá la configuración de la máquina y luego leerá cadenas para procesar. Para cada cadena, debe responder con ACEPTADA o RECHAZADA, según la ejecución de la máquina.

Input Format

Un alfabeto en la primera línea separado por espacios

Los estados en la siguiente línea separado por espacios

El estado inicial

Los estados finales separados por espacios

Las transiciones en formato "estado,símbolo->estado" separado por espacios

Cantidad de cadenas, N

cadena 1

cadena 2

... cadena N

Constraints

El alfabeto consiste en símbolos separados por espacios. El espacio no se permite como símbolo.

Los estados están separados por espacios.

Las transiciones están compuestas de los estados del AFD.

La cadena lambda se representa por &

Output Format

RECHAZADA o ACEPTADA según cadenas de entrada, una por línea

Sample Input 0

a b
q0 q1 q2
q0
q0 q2
q0,a->q0 q0,b->q1 q1,a->q1 q1,b->q2 q2,a->q1 q2,b->q1
2
aabab
aababa
Sample Output 0

ACEPTADA
RECHAZADA
Explanation 0

VER 2.1 EJEMPLO 1

Sample Input 1

a b
q0 q1 q2
q0
q1
q0,a->q1 q0,b->q2 q1,a->q1 q1,b->q2 q2,a->q2 q2,b->q2
4
a
ab
aaa
&
Sample Output 1

ACEPTADA
RECHAZADA
ACEPTADA
RECHAZADA

## Analisis
Para la primera linea necesitamos un alfabeto, es decir que debemos hacer verificaciones posteriores al alfabeto, una debe ser que la cadena solo contenga los caracteres que estan en el alfabeto, para capturar este alfabeto utilizaremos la funcion
```
alfabeto = input().split()
```
esta linea me permitira capturar espacios de separacion y meter los caracteres en una lista, asi para todos menos las cadenas y el estado inical.
como cosa importante vemos las transcisiones, para la primera entrada o input 0 tenemos la descripcion para el mapa del automata
```
q0,a->q0 q0,b->q1 q1,a->q1 q1,b->q2 q2,a->q1 q2,b->q1
```
y tenemos la construccion del mismo aqui
![Imagen automata finito determinista ejemplo 0](/DiseñoAfd/img/Captura%20de%20pantalla%202024-09-21%20192729.png)