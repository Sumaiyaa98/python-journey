import requests
import json

def load_data():
    try:

        with open("mydictionaryWords.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("mydictionaryWords.txt",'w') as file:
        return json.dump(data,file,indent=4)

def dictionary_lookup(user_input):
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_input}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        word = data[0]["word"]
        phonetic = data[0]["phonetic"]
        part_of_speech = data[0]["meanings"][0]["partOfSpeech"]
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        return word,phonetic,part_of_speech,definition
    else:
        raise Exception("Word not found. Check spelling!")
    
        
    



def main():
    all_words = load_data()
    while True:

        user_input = input("Enter a word to search the meaning (or type 'exit'): ").lower()
        if user_input == "exit":
            break
     
        try:
            word,phonetic,part_of_speech,definition = dictionary_lookup(user_input)
            print(f"Word: {word}\nPhonetic: {phonetic}\nPart of speech: {part_of_speech}\nDefinition: {definition}")
            

            word_info = {
                "word": word,
                "phonetic": phonetic,
                "part_of_speech": part_of_speech,
                "definition": definition
            }

            all_words.append(word_info)
            save_data(all_words)

        except Exception as e:
            print(str(e))

        


if __name__ == "__main__":
    main()