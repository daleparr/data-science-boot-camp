"""

import math as m
 
x = m.sqrt(64.25478)
print (x)

"""

def addition (x,y): # we have created a function called addition

    # the logic of the function goes here
    value = x + y
    return value

x = int(input("What is the number? "))
y = int(input("What is the next number? "))

total = addition(x,y)
print(total)

"""



def factorial(n):

    #two simple steps to creating a recursive function
    # step one - find the base case, the simplest version of our problem
    # step two - work towards the base case, whoch will end out recursion

    if n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)
    
print(factorial(10)) # Ouput  = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800



lambda : print("hello world!")
#this is a simple lambda function

greeting = lambda : print("why hello there")
greeting()



add_two = lambda x : x + 2
print(add_two(10)) #output : 12

cube = lambda y : y ** 3
print(cube(7)) #output 343

"""


