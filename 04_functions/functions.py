# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

def square(num):
   return num ** 2

print(square(4))

# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

def num_sum(a,b):
   return int(a)+int(b)

print(num_sum('2',3))


# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def mul(x,y):
   return x * y

print(mul(4,3))


# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circle(radius):
   circum = 2*math.pi*radius
   area = math.pi*(radius**2)
   return circum, area
   

a,b = circle(4)
print("Circumference:",a.__round__(2),"Area:",b.__round__(2))

# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
def greeting(user='User'):
   return 'Hello '+ user + '!'

print( greeting('Mike'))

# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.


cube = lambda x: x ** 3

print(cube(2))

# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_fun(*args):
    # print(args)
    # for i in args:
    #     print(i * 2)
    return sum(args)

print(sum_fun(1, 2))