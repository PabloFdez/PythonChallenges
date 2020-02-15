"""
Beginner Python exercises:
https://www.practicepython.org/

File Overlap
https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real
thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

"""
file1 = 'file1.txt'
file2 = 'file2.txt'
f1 = open(file1, 'r')
f2 = open(file2, 'r')

list1 = str(f1.read()).split("\n")
list2 = str(f2.read()).split("\n")

print(list1)
print(list2)

res = [x for x in list1 if x in list2]

print(res)

f1.close()
f2.close()