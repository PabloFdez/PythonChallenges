"""
Beginner Python exercises:
https://www.practicepython.org/

Fibonacci
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1.597

def askUserANumber():
    print("  -- Fibonnaci Creator --  ")
    return int(input("Please, Introduce the number of Fibonnaci no. to obtain: "))

def fibonnaciSeries(num):
    i = 0
    init = 1
    sigInit = 1
    stop = False
    serie = []

    while i < num:
        serie.append(init)
        serie.append(sigInit)
        init = init + sigInit
        sigInit = init + sigInit
        i += 1

    return serie[0:num]


print(fibonnaciSeries(askUserANumber()))