"""
Beginner Python exercises:
https://www.practicepython.org/

Rock Paper Scissors
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of
 congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

 - Rock beats scissors
 - Scissors beats paper
 - Paper beats rock

"""

print(" ~~~ Rock Paper Scissors ~~~ ")
print("      - Rock     = 1")
print("      - Scissors = 2")
print("      - Paper    = 3")

p1 = int(input("Player 1, introduce your choice [number]: "))
p2 = int(input("Player 2, introduce your choice [number]: "))
rePlay = 'y'

while rePlay == 'y':
    if (p1 == 1 and p2 == 1) or (p1 == 2 and p2 == 2) or (p1 == 3 and p2 == 3):
        print("Empate!")
        rePlay = input("Otra partida?[y/n]: ")
        if rePlay == 'y':
            p1 = int(input("Player 1, introduce your choice [number]: "))
            p2 = int(input("Player 2, introduce your choice [number]: \n"))

    if (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 3) or (p1 == 3 and p2 == 1):
        print("Gana el Player 1!")
        rePlay = input("Otra partida?[y/n]: ")
        if rePlay == 'y':
            p1 = int(input("Player 1, introduce your choice [number]: "))
            p2 = int(input("Player 2, introduce your choice [number]: \n"))

    if (p2 == 1 and p1 == 2) or (p2 == 2 and p1 == 3) or (p2 == 3 and p1 == 1):
        print("Gana el Player 2!")
        rePlay = input("Otra partida?[y/n]: ")
        if rePlay == 'y':
            p1 = int(input("Player 1, introduce your choice [number]: "))
            p2 = int(input("Player 2, introduce your choice [number]: \n"))
