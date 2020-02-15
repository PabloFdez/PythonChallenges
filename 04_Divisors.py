"""
Beginner Python exercises:
https://www.practicepython.org/

Divisors
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

# Imprime los 10 primeros divisores (si los tiene)
num = input("Introduce un numero :")
divisor = 1
i = 0

while i < 10:
    if (int(num) % divisor == 0):
        print("El numero ["+str(divisor)+"] es divisor de "+num+".")
        i += 1
    if divisor == int(num):
        exit()
    divisor += 1

