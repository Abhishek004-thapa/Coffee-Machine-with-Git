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
            print(f"We don't have enough {ingred}!!! Try another coffee.")
            is_resource_suff = False
    
    return is_resource_suff 
        
            
