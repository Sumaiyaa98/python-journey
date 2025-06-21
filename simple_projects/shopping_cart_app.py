def add_item(product_name_list, product_price_list, cart):
    while True:
        try:
            quantity = int(input("Enter the quantity of products you want to add: "))
            break
        except ValueError:
            print("Invalid quantity, digits only.")

    for j in range(quantity):
        name = input('Enter the name of product: ')
        product_name_list.append(name)
        while True:
            try:
                price = int(input('Enter the price of product: '))
                break
            except ValueError:
                print("Invalid price, digits only.")
        product_price_list.append(price)
        cart[name] = price  # Update cart here directly


def remove_item(product_name_list, product_price_list, cart):
    print("\n***** Remove Item from Cart *****")
    delete_name = input("Enter the name of the product to remove: ")
    found = False

    for key in list(cart.keys()):
        if key.lower() == delete_name.lower():
            found = True
            cart.pop(key)
            if key in product_name_list:
                idx = product_name_list.index(key)
                product_name_list.pop(idx)
                product_price_list.pop(idx)
            print(f"\n'{key}' has been deleted from your cart.")
            break

    if not found:
        print(f"\nNo product exists with the name '{delete_name}'.")


def view_current_cart(cart):
    if not cart:
        print("\n🛒 Your cart is empty.")
        return
    print("\n📦 Current Cart Items:")
    for key, val in cart.items():
        print(f" - {key.title()}: ${val}")


def show_total_amount(cart):
    if not cart:
        print("\n🛒 Your cart is empty.")
        return

    total_price = sum(cart.values())
    print(f"\n💰 Total Amount: ${total_price}")


def main():
    cart = {}
    product_name_list = []
    product_price_list = []

    while True:
        print("\n🛍️ Welcome to the Shopping Cart App | Choose an option:")
        print('1 - Add item to cart')
        print('2 - Remove item')
        print('3 - View current cart')
        print('4 - Show total amount')
        print('5 - Exit')

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                add_item(product_name_list, product_price_list, cart)
            case '2':
                remove_item(product_name_list, product_price_list, cart)
            case '3':
                view_current_cart(cart)
            case '4':
                show_total_amount(cart)
            case '5':
                print("Thank you for shopping with us. Goodbye!")
                break
            case _:
                print("⚠️ Invalid Choice, please try again.")


if __name__ == '__main__':
    main()
