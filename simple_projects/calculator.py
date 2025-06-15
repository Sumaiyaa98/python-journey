def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter the number correctly (digits only).")

def addition():
    num1 = get_number("Enter first num: ")
    num2 = get_number("Enter second num: ")
    print(f"\nAddition\n{num1} + {num2} = {num1 + num2:.2f}")

def subtraction():
    num1 = get_number("Enter first num: ")
    num2 = get_number("Enter second num: ")
    print(f"\nSubtraction\n{num1} - {num2} = {num1 - num2:.2f}")

def multiplication():
    num1 = get_number("Enter first num: ")
    num2 = get_number("Enter second num: ")
    print(f"\nMultiplication\n{num1} * {num2} = {num1 * num2:.2f}")

def division():
    num1 = get_number("Enter first num: ")
    while True:
        num2 = get_number("Enter second num (non-zero): ")
        if num2 != 0:
            break
        print(f"Invalid Number, {num1} can't be divided by ZERO.")
    print(f"\nDivision\n{num1} / {num2} = {num1 / num2:.2f}")

def main():
    while True:
        print("*" * 70)
        print("\nMINI CALCULATOR | CHOOSE AN OPTION")
        print('1- Add')
        print('2- Subtract')
        print('3- Multiply')
        print('4- Divide')
        print('5- Exit\n')
        print("*" * 70)

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                addition()
            case '2':
                subtraction()
            case '3':
                multiplication()
            case '4':
                division()
            case '5':
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid Choice! Please try again.")

if __name__ == '__main__':
    main()




# The function get_number(prompt) doesn't need to be passed into other functions. You just call it directly wherever you need user input.

# 📌 How it works:
# Let’s say you write this inside your addition() function:


# num1 = get_number("Enter first number: ")
# num2 = get_number("Enter second number: ")
# This means:

# The function get_number() is called right there.

# It asks the user for a number.

# It returns the number back to num1 and num2.

# So it’s like this:

# def addition():
#     num1 = get_number("Enter first number: ")  # it runs the input inside get_number
#     num2 = get_number("Enter second number: ") # again runs it for the second input
#     print(num1 + num2)
# You are not passing get_number as a parameter, you're simply using (or invoking) it wherever needed, just like using input() or print().

