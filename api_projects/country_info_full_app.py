import requests
import json
import os


def load_data():
    try:
        with open('countryInfoFinderApp.txt','r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(info):
    with open('countryInfoFinderApp.txt','w') as file:
        json.dump(info,file,indent=4)



def  search_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        common_name = data[0]['name']['common']
        official_name = data[0]['name']['official']
        region = data[0]['region']
        capital = data[0]['capital'][0]
        population = data[0]['population']
        currency = data[0]['currencies']
        languages = data[0]['languages']
        return common_name,official_name,region,capital,population,currency,languages
    else:
        raise Exception("Country Details not found! Check spelling again")


def  view_list():
    if not os.path.exists('countryInfoFinderApp.txt'):
        print("No Saved Country Info yet.")
        return
    
    with open('countryInfoFinderApp.txt','r') as file:
        try:
            country = json.load(file)
        except json.JSONDecodeError:
            print("Error reading saved country info.")
            return
        
    if not country:
        print('Country Info list is empty.')
    else:
        for i, country in enumerate(country, start=1):
            print(f"{i}-{country['Name']} Country Info \nOfficial Name: {country['Official Name']}\nRegion: {country['Region']}\nPopulation: {country['Population']}\nCurrency: {country['Currency']}\nLanguages: {country['Languages']}")

def delete_country_info():
    all_data = load_data()

    if not all_data:
        print("No data to delete.")
        return

    print("\nSaved Countries:")
    for i, country in enumerate(all_data, start=1):
        print(f"{i}- {country['Name']}")

    try:
        idx = int(input("Enter the index of the country to delete: ")) - 1
        if 0 <= idx < len(all_data):
            deleted = all_data.pop(idx)
            save_data(all_data)
            print(f"{deleted['Name']} has been deleted from the list.")
        else:
            print("Invalid index. No country deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    all_data = load_data()
    while(True):
        print("\nWelcome to Country Info Finder App | Choose an Option")
        print("1- Search Country Info")
        print("2- View List of Searched Country")
        print("3- Delete country detail from saved List")
        print("4- Exit\n")
        choice = input("Enter your choice: ")
        match(choice):
            case '1':
                print("Welcome to Search Country Info!")
                while True:

                    country_name = input("Enter a country name | (or type 'exit') : ").lower()
                    if country_name == 'exit':
                        break
                    try:
                        common_name,official_name,region,capital,population,currency,languages = search_country_info(country_name)
                        print(f"Name: {common_name}\n🇺🇳 Official Name: {official_name}\nRegion: {region}\nCaptial City: {capital}\nPopulation: {population}\nCurrency: {currency}\nLanguages: {languages}")
                        countr_info = {
                        'Name': common_name,
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
                    
            case '2':
                view_list()
            case '3':
                delete_country_info()
            case '4':
                break
            case _:
                print("Invalid Choice")


if __name__ == '__main__':
    main()

