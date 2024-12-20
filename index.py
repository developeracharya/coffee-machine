from main import MENU

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee" : 100,
    "money" : 0
}

COINS = {"quarters" : 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01 }
pocket = {"quarters" : 0, "dimes": 0, "nickles": 0, "pennies": 0 }
def coffeeResource(MENU, userNeed):

    for coffee, ingredients in MENU.items():
        if userNeed == coffee:
            return {coffee: ingredients}

def moneyCalculator(pocket):
    global COINS
    userPocket = 0
    for coin, quantity in pocket.items():
        userPocket += COINS[coin] * quantity
    return userPocket



continueOrder = True
orderHistory = []
while continueOrder:
    userNeed = input("What would you like (espresso/latte/cappuccino): ").lower()
    if userNeed == "report":
        for resource, quantity in resources.items():
            print(f"{resource}: {quantity}")
            continue
        continue

    orderInstance = coffeeResource(MENU, userNeed)
    orderHistory.append(orderInstance)
    ingredients = orderInstance[userNeed]["ingredients"]

    if resources["Water"] > ingredients["water"]:
        if resources["Coffee"] > ingredients["coffee"]:
            for coin  in pocket:
                pocket[coin] = int(input(f"How many {coin}?: "))
            userPocket = moneyCalculator(pocket)

            if userPocket >= orderInstance[userNeed]['cost']:
                print(f"Here is {userPocket - orderInstance[userNeed]["cost"]}in change.")
                print(f"Here is your {userNeed} ☕️ Enjoy!")
            else:
                print("Sorry that's not enough money. Money Refunded.")
        else:
            print("Sorry there is not enough Coffee.")
    else:
        print("Sorry there is not enough water.")
