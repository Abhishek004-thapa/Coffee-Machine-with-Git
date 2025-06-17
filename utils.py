from resources_db import machine_resources as resources
from resources_db import COFFEE_MENU


def get_resources_report():
    print(f"Water: {resources.get('water', ' ')}ml")
    print(f"Milk: {resources.get('milk', ' ')}ml")
    print(f"Coffee: {resources.get('coffee', ' ')}gm")
    print(f"Money: ${resources.get('money', ' ')}")
    
def is_resource_sufficient(choice):
    is_resource_suff = True
    for ingred, qty in COFFEE_MENU.get(choice, {}).get("ingredients", {}).items():
        if resources.get(ingred, 0) < qty:
            print(f"Sorry there is not enough {ingred}.")
            is_resource_suff = False
            break
    
    return is_resource_suff 

def process_coins(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    cost = COFFEE_MENU.get(choice, {}).get("money", " ")
    
    if total>cost:
        print(f"Here is ${round(total - cost, 2)} in change 💰.")
        print(f"Here is your {choice}☕. Enjoy!")
        
        if "money" in resources and isinstance(resources.get("money", " "), (float, int)):
            resources["money"] += cost
    
        else:
            print("KEYERROR !!! 'money' is not found as key in resouces.")
        
        for ingred, qty in COFFEE_MENU.get(choice, {}).get("ingredients", {}).items():
            resources[ingred] -= qty
    else:
        print("Sorry that's not enough money. Money refunded.")
    
        
            
