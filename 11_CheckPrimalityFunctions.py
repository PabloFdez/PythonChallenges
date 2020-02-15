"""
Beginner Python exercises:
https://www.practicepython.org/

List Overlap Comprehensions
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.

"""
import warnings

# Aprovecho para refrescar el uso de funciones
# Numeros primos
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71...

def pedirNumero ():
    num = input("Introduzca un numero entero :")

    if num.isdigit():
        return num
    if num.isalpha() or num.isascii() or num.isdecimal():
        warnings.warn("Valor introducido NO valido.")
        exit()

def comprobarSiNumPrimo (i):
    if i == 1:
        print("Numero introducido NO es primo.")
        exit()

    for div in range(2,i):
        if i%div == 0 and i != div:
            print("Numero introducido NO es primo.")
            exit()

    print("Numero introducido ES primo.")

comprobarSiNumPrimo(int(pedirNumero()))

