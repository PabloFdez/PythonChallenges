"""
Beginner Python exercises:
https://www.practicepython.org/

Odd or Even
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
    - If the number is a multiple of 4, print out a different message.
    - Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check
      divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""
print(" --- Comprobador de numeros --- \n")
numero = input("Introduzca un numero entero: ")

if int(numero) % 2 == 0 :
    print(" El numero introducido ["+numero+"] es Par.\n")
elif int(numero) % 4 == 0 :
    print(" El numero introducido ["+numero+"] es Par y multiplo de 4.\n")
else:
    print(" El numero introducido ["+numero+"] es Impar.\n")

print(" --- Comprobador de divisores --- \n")
divisor = input("Introduzca un divisor entero: ")
dividendo = input("Introduzca un dividendo entero: ")

if int(dividendo) % int(divisor) == 0 :
    print(" El  divisor introducido ["+divisor+"] divide SIN resto al dividendo ["+dividendo+"] .\n")
else:
    print(" El  divisor introducido ["+divisor+"] divide CON resto al dividendo ["+dividendo+"] .\n")