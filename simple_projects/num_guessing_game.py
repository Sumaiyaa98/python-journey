import random



def start_game():
    random_num = random.randint(1,100)
    guess_count = 5
    while(guess_count > 0):
        while(True):
            try:
                user_input = int(input("Guess a number between 1 to 100: "))
                break
            except ValueError:
                print("Invalid Input, Enter Digits only")
        guess_count -= 1
        
        if user_input == random_num:
            print("Right guess")
            break
        elif user_input > random_num:
            print(f"Too High\nguesses left: {guess_count}")
        else:
            print(f"Too Low\nguesses left: {guess_count}")
    else:
        print(f"Out of guesses, correct number was {random_num}")

def main():
    
    while(True):
        print("WELCOME TO NUMBER GUESSING GAME | CHOOSE AN OPTION")
        print("1-START A NEW GAME")
        print("2-Exit")
        choice = input("Enter a choice: ")
        if choice == '1':
            start_game()
        elif choice == '2':
            break
        else:
            print("INVALID INPUT")

            

if __name__ == "__main__":
    main()

    