import pyfiglet

# Resources
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
    "money": 0.0,
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}

machine_state = True
#print ascii art
logo = pyfiglet.figlet_format("Coffee Machine")
print(logo)

# Todo: 1. Prompt user by asking "What would you like? "
def select_coffee_drink(MENU):
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink in MENU:
            #print(f"{drink}, costs ${beverage[drink]:.2f}")
            return f"{drink}"
        else:
            print("Invalid Input: Type 'espresso', 'latte', or 'cappuccino'")

# Todo: 2. Print beverage_ingredients report
def print_report(resources) -> None:
    '''Prints current inventory of resources'''
    print("Current Inventory:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


# Todo: 3. Check if resources are sufficient
def check_resources(coffee_drink) -> bool:
    '''Checks if there are sufficient resources to make the selected drink'''
    drink_ingredients = MENU[coffee_drink]["ingredients"]

    for item in drink_ingredients:
        if resources[item] < drink_ingredients[item]:
            print(f"Sorry, there is not enough {item} to make your {coffee_drink}.")
            return False

    return True

# Todo: 4. Process coins
def process_payment(coffee_drink) -> float:
    '''process payment and return total amount inserted'''
    print(f"Please insert ${MENU[coffee_drink]['cost']:.2f} in coins to pay for the {coffee_drink}")
    try:
        total_pennies = int(input("How many pennies?: ")) * coins["pennies"]
        total_nickles = int(input("How many nickel(s)?: ")) * coins["nickels"]
        total_dimes = int(input("How many dime(s)?: ")) * coins["dimes"]
        total_quarters = int(input("How many quarter(s)?: ")) * coins["quarters"]

        # Calculate total AFTER all inputs
        total_coins = total_pennies + total_nickles + total_dimes + total_quarters
        return total_coins

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0.0  # Return 0 if invalid input


# Todo: 5. Check if transaction is successful
def check_transaction_status(total_coins_inserted, coffee_drink) -> bool:
    '''Check if payment is sufficient and process the transaction'''
    drink_cost = MENU[coffee_drink]["cost"]
    drink_ingredients = MENU[coffee_drink]["ingredients"]

    # Check if payment is sufficient
    if total_coins_inserted >= drink_cost:
        print(f"Here is your {coffee_drink}. Enjoy!")
        resources["money"] += drink_cost
        # Deduct resources from inventory
        resources["water"] -= drink_ingredients.get("water", 0)
        resources["milk"] -= drink_ingredients.get("milk", 0)
        resources["coffee"] -= drink_ingredients.get("coffee", 0)

        # Calculate and provide change if any
        change = total_coins_inserted - drink_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded: ${total_coins_inserted:.2f}")
        return False


# Todo: 6. Make Coffee drink
def prepare_drink() -> None:
    '''Handle the complete drink preparation workflow'''
    coffee_drink = select_coffee_drink(MENU)  # User selects drink

    if coffee_drink in ("espresso", "latte", "cappuccino"):
        # Step 1: Check if resources are sufficient
        if not check_resources(coffee_drink):
            return  # Exit if insufficient resources

        # Step 2: Process payment in coins
        total_coins_inserted = process_payment(coffee_drink)

        # Step 3: Check if payment was cancelled (invalid input)
        if total_coins_inserted == 0:
            print("Payment cancelled.")
            return

        # Step 4: Check transaction and make drink
        check_transaction_status(total_coins_inserted, coffee_drink)


# Turn off machine by entering "off" to the prompt
def turn_off() -> None:
    global machine_state
    if user_choice =="off":
        machine_state = False
        print("Turning off the coffee machine. Goodbye!")

# Main program loop
while machine_state:
    user_choice = input("\nWhat would you like to do? (order/report/off): ").lower()

    if user_choice == "order":
        prepare_drink()
    elif user_choice == "report":
        print_report(resources)
    elif user_choice == "off":
        turn_off()
    else:
        print("Invalid option. Please choose 'order', 'report', or 'off'.")
