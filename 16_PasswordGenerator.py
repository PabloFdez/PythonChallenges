"""
Beginner Python exercises:
https://www.practicepython.org/

Password Generator
https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers,
and symbols. The passwords should be random, generating a new password every time
the user asks for a new password. Include your run-time code in a main method.

Extra:

 - Ask the user how strong they want their password to be.
   For weak passwords, pick a word or two from a list.

"""
import random

def selectorDeNivel():
    print("  -- Generador de Contraseñas --  \n")
    print("  Seleccione el nivel de seguridad de la contraseña: ")
    print("          [Nivel de Seguridad Alto] = 1 ")
    print("          [Nivel de Seguridad Bajo] = 0 ")
    num = int(input("  Introduzca su selección: "))

    if (num != 0) and (num != 1):
        print(" [ERROR]: Introduzca un valor de nivel de seguridad apropiado.")
        exit()

    return num

def genLowLevel():
    listaPass = ['admin','1234','abcd','user','pass','hacker','password','987','0000','myPass','xyz']

    return str(listaPass[random.randrange(0,11)])+str(listaPass[random.randrange(0,11)])

def genHighLevel():
    # Longitud de la Pass se genera de forma aleatoria y puede variar entre 10 a 15
    longPass = random.randrange(12,18)
    i = 0

    # Guardamos las letras
    vocMinus = ['a', 'e', 'i', 'o', 'u']
    vocMayus = [i.upper() for i in vocMinus]
    consMinus = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x','y', 'z']
    consMayus = [i.upper() for i in consMinus]

    # Guardamos los numeros y signos
    nums = list(range(0, 10))
    signos = ['¡', '!', '?', '¿', '_', '-', '@', '.', ',']
    miPass = ""

    while i < longPass:
        auxRand = random.randrange(1,7)
        # vocMinus
        if auxRand == 1:
            miPass = miPass + str(vocMinus[random.randrange(0,len(vocMinus))])
            i += 1
         # vocMayus
        if auxRand == 2:
            miPass = miPass + str(vocMayus[random.randrange(0,len(vocMayus))])
            i += 1
        # consMinus
        if auxRand == 3:
            miPass = miPass + str(consMinus[random.randrange(0,len(consMinus))])
            i += 1
        # consMayus
        if auxRand == 4:
            miPass = miPass + str(consMayus[random.randrange(0,len(consMayus))])
            i += 1
        # nums
        if auxRand == 5:
            miPass = miPass + str(nums[random.randrange(0,len(nums))])
            i += 1
        # signos
        if auxRand == 6:
            miPass = miPass + str(signos[random.randrange(0,len(signos))])
            i += 1

    return miPass

def generadorDePass(num):
    if num == 0:
        return genLowLevel()
    if num == 1:
        return genHighLevel()


print("Su nueva contraseña:\n" + "  " + generadorDePass(selectorDeNivel()))
