"""
Beginner Python exercises:
https://www.practicepython.org/

Remove duplicates
https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

 - Write two different functions to do this - one using a loop and constructing a list, and another using sets.
 - Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""
print("  -- Borrado de los duplicados --  \n")
print("Introduzca una lista con elementos duplicados")
print("en el siguiente formato: 1,2,2,3,5,5,8,8,9")

# Conversion:
#   - Primero pedimos una lista (STRING) y la parseamos a una LISTA
#   - Transformamos esa lista de STRINGS en una lista de ENTEROS
lista = input("miLista : ").split(",")
lista = [int(i) for i in lista]

# Los SETs son elementos de datos desordenados, sin duplicados e inmutables
# Simplemente añadiendo la lista con los duplicados ya devuelve el resultado deseado
miSet = set(lista)
print(miSet)

def eliminaDup(lista):
    res = []
    for i in lista:
        if i not in res:
            res.append(i)
    return res

print(eliminaDup(lista))