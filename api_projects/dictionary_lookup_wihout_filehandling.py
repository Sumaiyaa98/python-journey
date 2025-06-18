import requests
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
    while True:

        user_input = input("Enter a name to search the meaning (or type 'exit'): ").lower()
        if user_input == "exit":
            break
     
        try:
            word,phonetic,part_of_speech,definition = dictionary_lookup(user_input)
            print(f"Word: {word}\nPhonetic: {phonetic}\nPart of speech: {part_of_speech}\nDefinition: {definition}")
            
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()