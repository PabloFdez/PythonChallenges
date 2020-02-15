"""
Beginner Python exercises:
https://www.practicepython.org/

List Less Than Ten
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:
    - Instead of printing the elements one by one, make a new list that has all the elements less
      than 5 from this list in it and print out this new list.
    - Write this in one line of Python.
    - Ask the user for a number and return a list that contains only elements from the original
      list a that are smaller than that number given by the user.

"""

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
pos = 0
pos2 = 0

for i in lista:
    if i < 5:
        print("El elemento ["+str(i)+"] en la posicion "+str(pos)+" de la lista es menor que 5.")
        pos2 += 1
    pos += 1

print("\n --- Extras 1 y 2: --- ")

# Primero necesitamos saber el numero de elementos de la nueva lista
# En vez de hacer otro bucle usamos un pos2 en el bucle anterior

lista2 = [0]*pos2   # Creamos una lista de 0s con el numero de elementos que necesitamos
pos3 = 0

for i in lista:
    if i < 5:
        lista2[pos3]=i
        pos3 += 1

print(lista2)

## Extra 2
# Estructura -> [output] for [item] in [list] if [filter]

print([number for number in lista if number < 5])

print("\n --- Extra 3: --- ")

numUsusario = input("Introduce un numero entero: ")
posE3 = 0
for i in lista:
    if i < int(numUsusario):
        print("El elemento ["+str(i)+"] en la posicion "+str(posE3)+" de la lista es menor que "+numUsusario+".")
    posE3 += 1