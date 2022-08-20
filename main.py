from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menus = Menu()
Coffee_Maker1 = CoffeeMaker()
money_machine1 = MoneyMachine()
end_machine = ""
lack_coins = False

def reset_conditions():
    """
    reset end_machine, lack_coins initial condition
    """
    global end_machine
    global lack_coins
    end_machine = ""
    lack_coins = False

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
"""
def check_ingridients(c):
    \"""
    string -> boolean
    check if there is enough ingridients \"\"\"
    return True
"""

def coin_dispenser():
    """
    void -> int
    prompt the user to enter a coins and produce the amount entered in int"""
    cash = 0

    while True:
        prompt = input("Insert Coins ")

        """coins is one of:
             - "quarters"
             - "dimes"
             - "nickels
             - "pennies"
          interp. represent the coins and their value
             - Quarters is $0.25
             - Dimes is $0.10
             - Nickels is $0.05
             - pennies is $0.01

        """
        if prompt == "quarters":
            cash = cash + 0.25
        elif prompt == "dimes":
            cash = cash + 0.10
        elif prompt == "nickels":
            cash = cash + 0.5
        elif prompt == "pennies":
            cash = cash + 0.1
        elif prompt == "done":
            break
        else:
            print("Invalid Input")
    return cash


def make_coffee(c):
    """produce coffee"""

    print("")


def make_order(s):
    """produce the coffee"""
    "!!!"
    global lack_coins
    global Coffee_Maker1
    global coffee_menus
    if Coffee_Maker1.is_resource_sufficient(coffee_menus.find_drink(s)):
        cash = coin_dispenser()
        make_coffee(s)
    else:
        lack_coins = True




while True:
    reset_conditions()
    print("What do you like?")
    print(coffee_menus.get_items())
    prompt = input("")
    selection(prompt)
    if end_machine == "break":
        break
    if lack_coins:
        continue
