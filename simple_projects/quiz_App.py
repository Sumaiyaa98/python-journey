def start_quiz():
    pass
def show_quiz_score():
    pass



def main():

    while(True):
        print("Welcome to Quiz App!|Choose Option")
        print('1-Start Quiz')
        print('2-Show Quiz Result')
        print('3-Exit')
        choice = input("Enter your Choice: ")
        match(choice):
            case '1':
                start_quiz()
            case '2':
                show_quiz_score()
            case '3':
                break
            case _:
                print("Invalid Choice")

if __name__ == '__main__':
    main()
