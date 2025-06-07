# conversion of datatypes
num = float(40)  # it will convert the int type to float
print(num)  #output: 40.0

x = int(2.45)
print(x) #output: 2

# repr() : use for clear representation and debugging and mainly use by developer. 
# str() :  represent as readable for human.
# print() : internally it use str() to get object and print it.

name = 'Alex'
print(str('Alex'))
print(repr('Alex'))
print('Alex')

print(1==2 or 2< 4) # exp-1, output: True 
print(1==2 and 2< 4) #exp-2 ,output: False  
print(1==2 < 4) #short form to write an exp like exp 2
 #and is used as a default that's why our output will be False

# 🔢 Binary, Octal, Hexadecimal Conversions in Python

# Convert decimal (base 10) to binary
print(bin(2))   # Output: 0b10
# Explanation:
# 2 in binary is 10
# '0b' is a prefix that Python uses to indicate a binary number

# Convert decimal to hexadecimal
print(hex(24))  # Output: 0x18
# Explanation:
# 24 in hexadecimal is 18 (1*16 + 8)
# '0x' is a prefix that Python uses to indicate a hexadecimal number

# Convert decimal to octal
print(oct(32))  # Output: 0o40
# Explanation:
# 32 in octal is 40 (4*8 + 0)
# '0o' is a prefix that Python uses to indicate an octal number

# ----------------------------------------------------------

# 👇 Another way: Convert string representation of a number in other bases to decimal

# Convert binary string '1000' to decimal
print(int('1000', 2))  # Output: 8
# Explanation:
# 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0 = 8

# Convert octal string '1000' to decimal
print(int('1000', 8))  # Output: 512
# Explanation:
# 1*8^3 + 0*8^2 + 0*8^1 + 0*8^0 = 512

# Convert hexadecimal string '1000' to decimal
print(int('1000', 16))  # Output: 4096
# Explanation:
# 1*16^3 + 0*16^2 + 0*16^1 + 0*16^0 = 4096

#to get random number, we can import the library of random
import random
print(random.random()) 
#to get random num in int
print(random.randint(1,10)) #meaans give me a random num between 1 to 10
print(random.randint(1,100))

#we also have random choice as well
#ex
arr = ['lemon','ginger','mint']
print(random.choice(arr)) #it will give the choices inside an array 

#we also have suffle option as well
random.shuffle(arr)
print(arr)  #output: ['ginger', 'mint', 'lemon']

setone = {1,2,3,5}
settwo = {1,3}

print(setone | settwo) #for union, output: {1, 2, 3, 5}
print(setone & settwo) #for intersection output:{1, 3}

#to know the type of datatype
print(type(setone))
print(type({})) #empty set is called dictionery
