import requests

def random_joke_generator():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        if joke_data:
            joke = joke_data["content"]
            return joke
        else:
            return "No jokes found."
    else:
        raise Exception("Failed to fetch Joke")
    
def main():
    try:
        joke = random_joke_generator()
        print(f"Joke: {joke}")
    except Exception as e:
        print(str(e))
    
if __name__ == '__main__':
    main()
