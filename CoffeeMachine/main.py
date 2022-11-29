##########################################################################
# Resources
##########################################################################
from machine_resources import resources, MENU


def display_report():
    """Prints the resources currently available in coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}mg")
    print(f"Money: ${'{:.2f}'.format(resources['money'])}")


def check_resources(user_command):
    """Checks if resources are available for the requested drink.
    Returns 'True' if resources available, otherwise lists the missing ingredient
    and returns "False". """
    for item in MENU[user_command]['ingredients']:
        if resources[item] < MENU[user_command]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def complete_transaction(user_command):
    """Requests payment in quarters, dimes, nickles, and pennies. Calculates total
    money inserted. If enough for purchase returns change and makes coffee. If not
    enough, refunds money and informs user."""
    print("Please insert coins.")
    money_paid = float(input("how many quarters: ")) * 0.25
    money_paid += float(input("how many dimes: ")) * 0.1
    money_paid += float(input("how many nickles: ")) * 0.05
    money_paid += float(input("how many pennies: ")) * 0.01
    if money_paid > MENU[user_command]['cost']:
        change = money_paid - MENU[user_command]['cost']
        print(f"Here is ${'{:.2f}'.format(change)} in change.")
        print(f"Here is your {user_command} ☕️. Enjoy!")
        for item in MENU[user_command]['ingredients']:
            resources[item] -= MENU[user_command]['ingredients'][item]
        resources['money'] += MENU[user_command]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")

##########################################################################
# Requirements List
##########################################################################
# TODO: 1. Prompt user by asking "what would you like? (espresso/latte/cappuccino):"
# TODO: 2. Turn off the coffee machine by entering "off" to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful.
# TODO: 7. Make Coffee.


machine_on = True
while machine_on:
    command = input("What would you like? espresso/latte/cappuccino): ")

    if command == "off":
        machine_on = False
    elif command == "report":
        display_report()
    elif command == "espresso" or "latte" or "cappuccino":
        if check_resources(command):
            complete_transaction(command)
