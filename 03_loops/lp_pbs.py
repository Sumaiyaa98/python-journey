# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_num_count = 0
for i in numbers:
    if i > 0:
        positive_num_count += 1
print("Final Count:",positive_num_count)


# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
n = 5
sum = 0
for i in range(1,n+1):
    if i%2==0:
        sum += i
        

print("Sum of even numbers from 0 to",n,"is",sum)


# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = 5
for i in range(1,11):
    if i==5:
        continue
    print(num,"*",i,"=",num*i)
   
# 4. Reverse a String
# Problem: Reverse a string using a loop.
name = 'Alex'
rev_string = ''
for x in name:
    rev_string =  x + rev_string
print(rev_string)


# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
user_string = 'javascript'

for char in user_string:
    if user_string.count(char) == 1:
        print(char)
        break


# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

my_num = 5
fact = 1
i = 1

while i <= my_num:
    fact *= i
    i += 1

print(fact)  

#another way

number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)


# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

#code
# while True:
#     userNum = int(input('Enter a num between 1 to 10: '))
#     if 1<= userNum <= 10:
#         print("Correct Input")
#         break
#     else:
#         print("Invalid Input, try again: ")
        
    

# 8. Prime Number Checker
# Problem: Check if a number is prime.

user_input = 20  # The number we want to check
is_prime = True  # We assume it's prime unless we find a factor

# Prime numbers are greater than 1
if user_input > 1:
    # Check for factors from 2 to user_input - 1
    for z in range(2, user_input):
        if (user_input % z) == 0:
            # If we find a number that divides it, it's not prime
            is_prime = False
            break  # Exit the loop early since it's confirmed not prime
else:
    # If number is 1 or less, it's not prime
    is_prime = False

print(is_prime)  # Output: True (if prime), False (if not prime)




# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]


items_list = ["apple", "banana", "orange", "apple", "mango"]
for item in items_list:
    if items_list.count(item) > 1:
        print('Duplicate Item:',item)
        break

#another method
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1