"""
Beginner Python exercises:
https://www.practicepython.org/

Write To A File
https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some
different code, use the code from the solution), and instead of printing the results to a screen, write the
results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

 - Ask the user to specify the name of the output file that will be saved.

"""

file_name = '/Users/PFD/Desktop/'+input(" Introduzca un nombre para el fichero: ")
f = open(file_name, 'a+')  # open file in append mode
content = input("\n   Escriba en el fichero: ")
f.write(content)
f.close()
