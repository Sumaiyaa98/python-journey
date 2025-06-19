import requests
import json

def load_data():
    try:
        with open('myNewsFile.txt','r') as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    

def save_data(news):
    with open('myNewsFile.txt','w') as file:
        json.dump(news,file,indent=4)


def news_headlines_app(countr_name):
    url = f"https://newsdata.io/api/1/news?apikey=pub_e2532dbf91a54aaa9fbf054dee939402&country={countr_name}&language=en"
    response = requests.get(url)
    data = response.json()
    if data["status"] == 'success':
        country = data['results'][0]['country'][0]
        news_title = data['results'][0]['title']
        news_category = data['results'][0]['category'][0]
        news_source = data['results'][0]['source_id']
        full_link = data['results'][0]['link']
        return country,news_title,news_category,news_source,full_link
    else:
        raise Exception("News not Found, Try Again")


def main():

    all_news = load_data()
    while True:

        countr_name = input("Enter a country code of country to see the news (Ex,Pakistan:pk) | (or type 'exit'): ").lower()
        if countr_name == 'exit':
            break
        try:
            country,news_title,news_category,news_source,full_link = news_headlines_app(countr_name)
            print(f"\nCountry Name: {country}\nNews Category: {news_category}\nNews Title: {news_title}\nSource: {news_source}\nFull Link: ({full_link})")

            my_news = {
                'Country Name': country,
                'News Category': news_category,
                'News Title': news_title,
                'Source': news_source,
                'Full Link': full_link

            }

            all_news.append(my_news)
            save_data(all_news)
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()