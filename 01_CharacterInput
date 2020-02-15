"""
Beginner Python exercises:
https://www.practicepython.org/

Character Input
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
    - Add on to the previous program by asking the user for another number and printing
      out that many copies of the previous message. (Hint: order of operations exists in Python)
    - Print out that many copies of the previous message on separate lines.
      (Hint: the string "\n is the same as pressing the ENTER button)

"""
import datetime

now = datetime.datetime.now()
#print(now.year)

nombre = input("Introduce tu nombre: \n")
edad = input("Introduce tu edad: \n")
iteraciones = input("Introduce un numero [1-5]: \n")
i=0

while i < int(iteraciones):
    print("Hola "+nombre + ", en el año "+str(now.year + (100-int(edad)))+" cumplirás 100 años!")
    i += 1
