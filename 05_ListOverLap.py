"""
Beginner Python exercises:
https://www.practicepython.org/

List Over Lap
https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

 - Randomly generate two lists to test this
 - Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""
from array import *
# Generamos listas aleatorias
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
nuevaLista = []

for i in a:
    if i in b:
        if i not in nuevaLista:
            nuevaLista.append(i)

print(nuevaLista)

# -- Extra 1 --
# Lista aleatoria de longitud aleatoria (entre 5 y 15) elementos [1-50]
print(" -- Extra 1 -- ")
lisRan1 = [random.randrange(1, 50) for i in range(random.randrange(5,15))]
print(lisRan1)

# Lista aleatoria de 7 elementos [1-50]
lisRan2 = random.sample(range(1, 50), 7)
print(lisRan2)

nuevaLista2 = []

for j in lisRan1:
    if j in lisRan2:
        if j not in nuevaLista2:
            nuevaLista2.append(j)

if len(nuevaLista2) != 0:
    print(nuevaLista2)
else:
    print("Las listas no comparten elementos iguales.")

## Extra 2
# Estructura -> [output] for [item] in [list] if [filter]
print(" -- Extra 2 -- ")

nuevaLista3 = []
[nuevaLista3.append(x) for x in a for y in b if x == y if x not in nuevaLista3]

print(nuevaLista3)

