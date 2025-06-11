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

# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def map_funtion(**kwargs):
   for key, value in kwargs.items():
        print(f"{key}: {value}")


map_funtion(name = 'Alix',age = 29)
map_funtion(name = 'Mike',age = 22,gpa=3.4)

# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    # Loop through even numbers from 2 to the given limit
    for i in range(2, limit + 1, 2):
        yield i  # 'yield' returns one value at a time and pauses the function until the next value is requested

# 'yield' vs 'return':
# - 'return' ends the function immediately and returns a single value
# - 'yield' returns a value, but pauses the function state
#   so that it can continue from the same point next time
# - This makes 'yield' very memory-efficient for large sequences

# Using the generator:
for num in even_generator(10):
    print(num)

# Output:
# 2
# 4
# 6
# 8
# 10


# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)