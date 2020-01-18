#Insert here the module/library import statements 
import io   
import sys
import math
print("El programa ejecutará e imprimirá la solución de todos los ejercicios hasta el final")
#Example:  

eggs = (1,3,8,3,2)
my_listComprehension = [1/egg for egg in eggs]
print("Ejemplo")
print(my_listComprehension)

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
cuadrados = [i**2 for i in range(1,20)]
print("Ejercicio 1")
print(cuadrados)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**i for i in range(1,50)]
print("Ejercicio 2")
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
raices = [math.sqrt(i) for i in range(1,100)]
print("Ejercicio 3")
print(raices)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
my_list = [i for i in (range(-10,1))]
print("Ejercicio 4")
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [i for i in range (0,100) if i%2 == 0]
print("Ejercicio 5")
print(odds)

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [i for i in range (0,100) if i%7 == 0]
print("Ejercicio 6")
print(divisible_by_seven)

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
teststring = 'Find all of the words in a string that are monosyllabic'

vocales = ["a", "e", "i", "o", "u"," "]
non_vowels = "".join([i for i in teststring if i not in vocales])
print("Ejercicio 7")
print(non_vowels)

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

frase = "The Quick Brown Fox Jumped Over The Lazy Dog"
capital_letters = "".join([i for i in frase if i.isupper()])
print("Ejercicio 8")
print(capital_letters)

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

frase = "The Quick Brown Fox Jumped Over The Lazy Dog"
vocales = ["a", "e", "i", "o", "u"," "]
consonantes = "".join([i for i in frase if i not in vocales])
print("Ejercicio 9")
print(consonantes)

#10. Find the folders you have in your datamad0120 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

import os
path = "/Users/soyungalgo/documents/github/datamad0120"
files = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
#files = os.listdir("/Users/soyungalgo/documents/github/datamad0120")
print("Ejercicio 10")
print(files)

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

import random
random_lists = [random.sample(range(100),10) for _ in range(4)]
print("Ejercicio 11")
print (random_lists)

#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [b for a in list_of_lists for b in a]
print("Ejercicio 12")
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]
floats = [float(b) for a in list_of_lists for b in a] #una lista
floats2 = [[float(b)for b in a]for a in list_of_lists] #lista de listas
print("Ejercicio 13")
print(floats)
print(floats2)

#14. Handle the exception thrown by the code below by using try and except blocks. 
print("Ejercicio 14")
for i in ['a','b',5]:
    try: 
        print (i**2)
    except TypeError:
        print("TypeError tienes que introducir un int")

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
print("Ejercicio 15")
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("No puedes dividir entre cero, amigx....")

#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio 16")
abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print("IndexError, el index está fuera de rango")

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

print("Ejercicio 17")
suma = 0
while True:
    try:
        #corregido, el problema es que suma += entrada estaba después del if
        entrada = int(input("Introduce números enteros y pulsa 1 cuando acabes "))
        suma += entrada
        if entrada == 1:
            break
    except ValueError as x:
        print("Has introducido", (x))
        print("Tienes que introducir un número entero")

print("La suma de los números es {}" .format(suma))

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio 18")
try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("No encuentro el archivo")
except io.UnsupportedOperation:
    print("No se puede escribir el archivo")

#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
print("Ejercicio 19")
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(f.strip())
except FileNotFoundError:
    print("El archivo no existe")
except AttributeError:
    print("Un string no tiene atributo strip ")
    
#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
print("Ejercicio 20")
def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
    except AssertionError:
        print("Esta función solo puede usarse en Linux")

linux_interaction()

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
print("Ejercicio 21")
def cuadradonum():
    while True:
        try:
            entrada = int(input("Introduce un número entero o un 0 si quieres salir: "))
            if entrada == 0:
                break
            print("El cuadrado del número es: ",entrada**2)   
        except ValueError as x:
            print("Has introducido", x)
            print("Tienes que introducir un número entero")

cuadradonum()
    
# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
print("Ejercicio 22")
divisible_list = [i for i in range (0,1000) if True in [True for  n in range(2,9) if i%n == 0]]
print(divisible_list)


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
print("Ejercicio 23")

class Error(Exception):
    pass

class Customiced(Error):
    pass
minimo = 2
Total_Marks = int(input("Enter Total Marks Scored: ")) 
notas = []
while len(notas)< Total_Marks:
    try:
        Num_of_Sections = int(input("Enter Num of Sections: "))
        if Num_of_Sections > minimo:
            notas.append(Num_of_Sections)
        else:
            raise Customiced

        
    except Customiced:
        print ("El número debe ser mayor que 2")
    except ValueError:
        print("Debes introducir un número entero")

print ("Has introducido {} notas." .format(Total_Marks))
print ("Las notas que has introducido son: ", (notas))



