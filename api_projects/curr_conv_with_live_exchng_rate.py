import requests
def currency_conv_with_live_exhange_rate(base_currency,target_currency,amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:

        from_currency = data['base']
        to_currency = data['rates'][f"{target_currency}"]
        converted_amount = amount*to_currency
        return from_currency,converted_amount
    else:
        raise Exception("Error, Please check spelling again!")
def main():
    base_currency= input("Enter base currency (e.g. USD): ").upper()
    target_currency = input("Enter target currency (e.g. PKR): ").upper()
    while True:
        try:
            amount = int(input("Enter amount to convert: "))
            if amount <= 0:
                print("Invalid amount,(Enter amount greater than zero)")
                continue
            break
                
        except ValueError:
            print("Invalid amount,(Enter digits only)")

    try:
        from_currency,converted_amount = currency_conv_with_live_exhange_rate(base_currency,target_currency,amount)
        print(f"💱 {amount} {from_currency} = {round(converted_amount, 2)} {target_currency}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
