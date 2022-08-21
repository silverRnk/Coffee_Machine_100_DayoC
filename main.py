from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menus = Menu()
Coffee_Maker1 = CoffeeMaker()
money_machine1 = MoneyMachine()
end_machine = ""
lack_ingridients = False
lack_coins = False


def reset_conditions():
    """
    reset end_machine, lack_coins initial condition
    """
    global end_machine
    global lack_coins
    global lack_ingridients
    end_machine = ""
    lack_coins = False
    lack_ingridients = False

def selection(s):
    """ enter a string, run a function based on input"""
    "s is one of:  off | report | Menu"
    global end_machine

    def menu(s):
        """
        string -> boolean
        produce true if s is either equal to one of menus"""

        global coffee_menus
        menus = coffee_menus.get_items()
        menus = menus.split("/")
        for i in menus:
            if i == s:
                return True
            else:
                continue
        return False

    if s == "off":
        end_machine = "break"
    elif s == "report":
        Coffee_Maker1.report()
        money_machine1.report()
    elif menu(s):
        make_order(s)
    else:
        print("Invalid Input")



def make_order(s):
    """produce the coffee"""
    "!!!"
    global lack_coins
    global lack_ingridients
    global Coffee_Maker1
    global coffee_menus
    global money_machine1

    current_order = coffee_menus.find_drink(s)
    if Coffee_Maker1.is_resource_sufficient(current_order):
        if money_machine1.make_payment(current_order.cost):
            Coffee_Maker1.make_coffee(current_order)
        else:
            lack_coins = True
    else:
        lack_ingridients = True




while True:
    reset_conditions()
    print("What do you like?")
    print(coffee_menus.get_items())
    prompt = input("")
    selection(prompt)
    if end_machine == "break":
        break
    if lack_coins or lack_ingridients:
        continue
