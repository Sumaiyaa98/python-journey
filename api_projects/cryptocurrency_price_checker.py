import requests

def cryptocurrency_price_check(coin_name):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if coin_name in data:
        coin_name = data[f"{coin_name}"]["usd"]
        return coin_name
    else:
        raise Exception("Coin not found. Check spelling or try a different one.")



def main():
   while True:
    coin_name = input("Enter a coin name (or type 'exit'): ").lower()
    if coin_name == "exit":
        break
    try:
        coin = cryptocurrency_price_check(coin_name)
        print(f"{coin_name}: {coin}USD ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()