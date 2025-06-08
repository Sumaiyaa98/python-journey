#to get the input from user
# name = input("Enter your name: ")
# print(name)

#user input is always the string datatype, so to convert the string into other types, we have to do it manually
#string to int
# gpa = int(input('Enter your Gpa: '))
# print(type(gpa))  


#conditionals problems
# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input('Enter your age: '))
if age <13:
    print('child')
elif age<20:
    print('Teenager')
elif age<59:
    print('Adult')
else:
    print('Senior')


