import requests

def random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        title = data["data"]["volumeInfo"]["title"]
        author = data["data"]["volumeInfo"]["authors"][0]
        publisher = data["data"]["volumeInfo"]["publisher"]

    #Handle missing fields:
    # Sometimes an API may return a book without authors or publisher. You can safely handle that like this:
    # author = data["data"]["volumeInfo"].get("authors", ["Unknown"])[0]
    # publisher = data["data"]["volumeInfo"].get("publisher", "Unknown")

        return title,author,publisher
    else:
        raise Exception("Data not found!")

def main():
    try:
        title,author,publisher = random_book()
        print(f"Title: {title}\nAuthor: {author}\nPublisher: {publisher}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

    

