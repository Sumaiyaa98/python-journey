import requests
import json

def load_data():
    try:

        with open('randomJoke.txt','r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def save_data(joke):
    with open('randomJoke.txt','w') as file:
        json.dump(joke,file,indent=4)


def random_joke_with_json():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        setup = data['setup']
        punchline = data['punchline']
        return setup,punchline
    else:
        raise Exception("Joke not found, Try Again!")


def main():
    all_jokes = load_data()
    print("Welcome to Random Joke Generator!")
    while True:
        userInput = input("Press enter to get a new joke | (or type 'exit')to exit: ")
        if userInput == 'exit':
            break
        try:
            setup,punchline = random_joke_with_json()
            print(f"{setup}\n{punchline}😄")

            joke = {
                'setup': setup,
                'punchline':punchline
            }

            all_jokes.append(joke)
            save_data(all_jokes)

        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()
