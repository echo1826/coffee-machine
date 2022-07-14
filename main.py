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
        process_espresso()
    elif choice == 'latte':
        process_latte()
    elif choice == 'cappuccino':
        process_cappuccino()
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


main()