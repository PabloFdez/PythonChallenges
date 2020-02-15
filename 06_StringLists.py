"""
Beginner Python exercises:
https://www.practicepython.org/

String Lists
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

"""
myStr = input("Introduza una frase :")

auxStr = myStr[::-1]
print(auxStr)

if myStr == auxStr:
    print("Has introducido un palindromo")
else:
    print("No has introducido un palindromo")
