from utils import get_resources_report, is_resource_sufficient, process_coins
    
is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_machine_on = False
        
    elif choice.lower() == "report":
        get_resources_report()
        
    else:
        if choice not in ["latte", "espresso", "cappuccino"]:
            print(f"Sorry!!! {choice} is not available. Select correctly")
        else:
            if is_resource_sufficient(choice):
                process_coins(choice)
        
