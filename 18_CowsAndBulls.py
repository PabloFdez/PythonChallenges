"""
Beginner Python exercises:
https://www.practicepython.org/

Cows and Bulls
https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
 · For every digit that the user guessed correctly in the correct place,
  they have a “cow”.
 · For every digit the user guessed correctly in the wrong place is a “bull.”

 Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
 Once the user guesses the correct number, the game is over.
 Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
   1234
  2 cows, 0 bulls
   1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""
import random

def comprobarFormatoIntento(num):
    if((num<1000) or (num>9999)):
        print(" [ERROR]: El numero debe tener 4 digitos.")
        exit()

def compruebaBulls(objetivo, intento):
    obLis = [int(x) for x in str(objetivo)]
    obInt = [int(x) for x in str(intento)]
    coinciden = [x for x in obLis if x in obInt]
    myBulls = 0
    myCows = 0

    for i in coinciden:
            if (obInt.index(i) == obLis.index(i)):
                myCows += 1
            else:
                myBulls += 1
    print(" Cows: " + str(myCows) + " Bulls: " + str(myBulls))
    if myCows == 4:
        print("  WINNER!!!!")
        return True

# Numero objetivo  de 4 digitos generado aleatoriamente
objetivo = random.randrange(1000,10000)
print(objetivo)

print("  -- Cows & Bulls game -- ")

finJuego = False
numCows = 0
numBulls = 0

while not finJuego:
    intento = int(input(" Introduza su intento [dddd]: "))
    comprobarFormatoIntento(intento)
    finJuego = compruebaBulls(objetivo, intento)

