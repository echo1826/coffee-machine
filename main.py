MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def main():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'espresso':
        process_order(MENU['espresso'])
    elif choice == 'latte':
        process_order(MENU['latte'])
    elif choice == 'cappuccino':
        process_order(MENU["cappuccino"])
    elif choice == 'report':
        report()
    elif choice == 'off':
        exit(1)
    else:
        print("Incorrect choice inputted.\nPlease try again.")
        main()
    main()


def report():
    print("Printing report...")
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}ml
    Money: ${profit}
    """)

def resource_check(order_ingredients):
    for ingredient_name in order_ingredients:
        if order_ingredients[ingredient_name] > resources[ingredient_name]:
            print(f"Sorry there is not enough {ingredient_name}.")
            return False
    return True

def ask_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)

    return round(total, 2)

def process_order(order):
    if not resource_check(order['ingredients']):
        main()
    


main()