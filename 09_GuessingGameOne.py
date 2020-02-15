"""
Beginner Python exercises:
https://www.practicepython.org/

Guessing Game One
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

"""
import random

num = random.randrange(1,10)
seguir = True

while seguir:
    numGuess = int(input("Adivina el numero [1-9]:"))
    if num > numGuess:
       print(("Uy! Casi... un pelin mas...\n"))
    if num < numGuess:
       print(("Ala! Te has pasado\n"))
    if num == numGuess:
       print(("¡¡Sii!! Ganaste!\n"))
       seguir = False
