from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
machine = CoffeeMaker()
register = MoneyMachine()
machine_on = True

while machine_on:
    response = input(f"What would you like {my_menu.get_items()}?: ")
    if response == "off":
        machine_on = False
    elif response == "report":
        machine.report()
        register.report()
    else:
        if my_menu.find_drink(response) is not None:
            machine.is_resource_sufficient(my_menu.find_drink(response))
            if register.make_payment(my_menu.find_drink(response).cost):
                machine.make_coffee(my_menu.find_drink(response))
