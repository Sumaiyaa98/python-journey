import requests
import json

def load_data():
    try:
        with open('countryInfoFinderApp.txt','r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(info):
    with open('countryInfoFinderApp.txt','w') as file:
        json.dump(info,file,indent=4)


def country_info_finder(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        official_name = data[0]['name']['official']
        region = data[0]['region']
        capital = data[0]['capital'][0]
        population = data[0]['population']
        currency = data[0]['currencies']
        languages = data[0]['languages']
        return official_name,region,capital,population,currency,languages
    else:
        raise Exception("Country Details not found! Check spelling again")

def main():

    all_data = load_data()
    print("Welcome to Country Info Finder App")
    while True:

        country_name = input("Enter a country name | (or type 'exit') : ").lower()
        if country_name == 'exit':
            break

        try:
            official_name,region,capital,population,currency,languages = country_info_finder(country_name)
            print(f"Official Name: {official_name}\nRegion: {region}\nCaptial City: {capital}\nPopulation: {population}\nCurrency: {currency}\nLanguages: {languages}")

            countr_info = {
                'Official Name': official_name,
                'Region': region,
                'Population': population,
                'Currency': currency,
                'Languages': languages

            }
            all_data.append(countr_info)
            save_data(all_data)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
