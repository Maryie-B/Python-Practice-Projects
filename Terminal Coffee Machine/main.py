from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options} : ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if order is not None:
            check = coffee_maker.is_resource_sufficient(order)
            if check:
                total = money_machine.make_payment(order.cost)
                if total:
                    coffee = coffee_maker.make_coffee(order)

