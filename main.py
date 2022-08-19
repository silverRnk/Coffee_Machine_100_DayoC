import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
"from money_machine import MoneyMachine"

coffee_menus = Menu()
Coffee_Maker1 = CoffeeMaker()


def selection(s):
    """ enter a string, run a function based on input"""
    "s is one of:  off| report | Menu"
    if s == "off":
        sys.exit()
    elif s == "report":
        Coffee_Maker1.report()
    else:
        make_order(s)


def make_order(s):
    """produce the coffee"""
    "!!!"
    return s


print("What do you like?")
print(coffee_menus.get_items())
prompt = input("")
selection(prompt)
