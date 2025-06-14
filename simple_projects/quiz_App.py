def start_quiz():
    print("\n*********Answer the Following Questions!*********\n")

    questions = [
        'What is the capital of France?',
        'What is 5 + 7?',
        'What is the highest mountain in the world?',
        'What does CPU stand for?',
        'What is the longest river in the world?'
    ]

    correct_ans = ['paris', '12', 'mount everest', 'central processing unit', 'nile']
    user_ans = []

    for i in questions:
        q = input(f"{i} ")
       
        user_ans.append(q.lower())
            

    quiz = {}
    for j in range(len(questions)):
        quiz[questions[j]] = user_ans[j]

    print('*' * 60)
    for idx, (question, answer) in enumerate(quiz.items()):
        print(f"\nQ: {question}\nYour Ans: {answer}\nCorrect Ans -> {correct_ans[idx]}")
    print('*' * 60)

    
    count = 0
    for i in range(len(user_ans)):
        if correct_ans[i] == user_ans[i]:
            count += 1

    result = (count / len(correct_ans)) * 100
    print(f"\nYour Score: {result}% ({count} out of {len(correct_ans)} correct)")




def main():

    while(True):
        print('*'*60)
        print("\nWelcome to Quiz App!|Choose Option")
        print('1-Start Quiz')
        print('2-Exit\n')
        print('*'*60)
        choice = input("Enter your Choice: ")
        match(choice):
            case '1':
                start_quiz()
            case '2':
                break
            case _:
                print("Invalid Choice")

if __name__ == '__main__':
    main()
