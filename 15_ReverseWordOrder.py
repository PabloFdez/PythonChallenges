"""
Beginner Python exercises:
https://www.practicepython.org/

Reverse Word Order
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.

"""

print("  -- Inversor de frases --  ")
frase = input("Introduce una frase: ")

def listaDePalabras(frase):
    return frase.split(" ")

def inversorDeListas(lista):
    return [lista[-i] for i in range(1, len(lista)+1)]

print(inversorDeListas(listaDePalabras(frase)))