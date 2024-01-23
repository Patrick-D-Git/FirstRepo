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

# Ingredients

water = 300
milk = 200
coffee = 100

# User's money

money = 0
change = 0
# COINS

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

# conditions
transaction_valid = True
prompt_loop = True


# TODO: 4. Calculate user coins totals


def convert_user_coins(user_quarters, user_dimes, user_nickles, user_pennies):
    total_user_coin = (user_quarters * QUARTERS) + (user_dimes * DIMES) + (user_nickles * NICKLES) + (user_pennies *
                                                                                                      PENNIES)
    return total_user_coin


# TODO 5. Check Ingredients


def check_ingredients(user_input, water_left, milk_left, coffee_left, enough_ingredients):
    enough_ingredients = True
    water_left = water - MENU[user_input]["ingredients"]["water"]
    milk_left = milk - MENU[user_input]["ingredients"]["milk"]
    coffee_left = coffee - MENU[user_input]["ingredients"]["coffee"]

    if water_left < 0:
        print("Sorry there is not enough water.")
        enough_ingredients = False
        return water_left, milk_left, coffee_left, enough_ingredients
    elif milk_left < 0:
        print("Sorry there is not enough milk.")
        enough_ingredients = False
        return water_left, milk_left, coffee_left, enough_ingredients
    elif coffee_left < 0:
        print("Sorry there is not enough coffee.")
        enough_ingredients = False
        return water_left, milk_left, coffee_left, enough_ingredients
    else:
        return water_left, milk_left, coffee_left, enough_ingredients


# TODO: 2. Print Report


def ingredient_report():
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee} g")
    print(f"Money: ${money}")


def calculate_payment(user_money, trans_is_valid):
    trans_is_valid = True
    if user_money < MENU[user_prompt]["cost"]:
        print("Sorry, your payment is not enough for this transaction.")
        trans_is_valid = False
        return user_money, trans_is_valid
    else:
        user_change = user_money - MENU[user_prompt]["cost"]
        return user_change, trans_is_valid


# TODO: 1. User Prompt
while prompt_loop:
    transaction_valid = True

    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while transaction_valid:

        if user_prompt == "report":
            ingredient_report()
            transaction_valid = False
        elif user_prompt == "off":
            prompt_loop = False
            break

        else:

            # TODO: 3. User Input Coins

            print("Please Insert Coins.")

            user_coin_quarter = float(input("How many quarters?: "))
            user_coin_dimes = float(input("How many dimes?: "))
            user_coin_nickles = float(input("How many nickles?: "))
            user_coin_pennies = float(input("How many pennies?: "))

            # user's total money placed
            user_total_money = round(convert_user_coins(user_coin_quarter, user_coin_dimes, user_coin_nickles,
                                                        user_coin_pennies),
                                     2)

            # Check if user have enough money to pay for coffee
            change, transaction_valid = calculate_payment(user_total_money, transaction_valid)

            if not transaction_valid:
                break

            # Check if we have enough ingredients to make coffee.
            ingredients_valid = True
            water, milk, coffee, ingredients_valid = check_ingredients(user_prompt, water, milk, coffee,
                                                                       ingredients_valid)

            if ingredients_valid:
                # Print change and coffee
                money += MENU[user_prompt]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_prompt} ☕️ Enjoy!")

        break
