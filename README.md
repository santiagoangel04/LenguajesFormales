# LenguajesFormales
Todo lo desarrollado en el curso de lenguajes formales tanto ejercicios como otros cosas

## Ejercicio 1: Taller de cadenas
### Subcadenas 

Dada una cadena, se debe extraer todas las subcadenas de dicha cadena. Por ejemplo, dado la cadena "java", todas las subcadenas son:
```
java

jav

ja

j

ava

av

a

va

v

a
```
Input Format
```
Hello
```

> [!NOTE]
> Constraints
> las subcadenas se ordenan usando primero los prefijos descendentes y luego los sufijos descendentes, una por línea

Output Format
```
Hello

Hell

Hel

He

H

ello

ell

el

e

llo

ll

l

lo

l

o
```
Sample Input 0
```
Hello
```
Sample Output 0
```
Hello
Hell
Hel
He
H
ello
ell
el
e
llo
ll
l
lo
l
o
```
Explanation 0

Primero se imprime "Hello" y todos sus prefijos en orden descendente, "Hell", "Hel", hasta "H". Luego se imprime el primer sufijo "ello" y todos sus prefijos descendentes, "ell", "el" y "e". Luego el siguiente sufijo "llo" con todos sus prefijos y sucesivamente hasta llegar al último sufijo "o"

Sample Input 1
```
Hola,Mundo!
```
Sample Output 1
```
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
ola,Mundo!
ola,Mundo
ola,Mund
ola,Mun
ola,Mu
ola,M
ola,
ola
ol
o
la,Mundo!
la,Mundo
la,Mund
la,Mun
la,Mu
la,M
la,
la
l
a,Mundo!
a,Mundo
a,Mund
a,Mun
a,Mu
a,M
a,
a
,Mundo!
,Mundo
,Mund
,Mun
,Mu
,M
,
Mundo!
Mundo
Mund
Mun
Mu
M
undo!
undo
und
un
u
ndo!
ndo
nd
n
do!
do
d
o!
o
!
```
Sample Input 2
```
Nivel,Dios!
```
Sample Output 2
```
Nivel,Dios!
Nivel,Dios
Nivel,Dio
Nivel,Di
Nivel,D
Nivel,
Nivel
Nive
Niv
Ni
N
ivel,Dios!
ivel,Dios
ivel,Dio
ivel,Di
ivel,D
ivel,
ivel
ive
iv
i
vel,Dios!
vel,Dios
vel,Dio
vel,Di
vel,D
vel,
vel
ve
v
el,Dios!
el,Dios
el,Dio
el,Di
el,D
el,
el
e
l,Dios!
l,Dios
l,Dio
l,Di
l,D
l,
l
,Dios!
,Dios
,Dio
,Di
,D
,
Dios!
Dios
Dio
Di
D
ios!
ios
io
i
os!
os
o
s!
s
!
```
[Codigo de solucion con documentacion](/Cadenas/subcadenas.py)

## Ejercicio 2: Taller de cadenas
### Prefijos 
Dada una cadena, se debe extraer todos los prefijos de dicha cadena. Por ejemplo, dado la cadena "java", todos los prefijos son:
```
java

jav

ja

j
```
Input Format
```
Hola,Mundo!
```
> [!NOTE]
> Constraints
la cadena no tendrá espacios
se imprime primero la cadena completa y luego los prefijos en orden descendente, una por línea

Output Format
```
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
```
Sample Input 0
```
Hola,Mundo!
```
Sample Output 0
```
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
```

Sample Input 1
```
Programacion
```
Sample Output 1
```
Programacion
Programacio
Programaci
Programac
Programa
Program
Progra
Progr
Prog
Pro
Pr
P
```
[Codigo de solucion con documentacion](/Cadenas/Prefijos.py)

