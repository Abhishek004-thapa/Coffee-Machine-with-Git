from resources_db import machine_resources as resources

def get_resources_report():
    print(f"Water: {resources.get('water', ' ')}ml")
    print(f"Milk: {resources.get('milk', ' ')}ml")
    print(f"Coffee: {resources.get('coffee', ' ')}gm")
    print(f"Money: ${resources.get('money', ' ')}")
    
is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_machine_on = False
        
    elif choice.lower() == "report":
        get_resources_report()
        
