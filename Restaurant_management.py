def add_item(menu, item):
    menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        return f"{item} does not exist in the menu."
    return menu

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

#input
initial_menu = input("Enter initial menu items separated by commas: ").split(",")
add_item_input = input("Enter item to add: ")
remove_item_input = input("Enter item to remove: ")
check_item_input = input("Enter item to check: ")

initial_menu = add_item(initial_menu, add_item_input)
initial_menu = remove_item(initial_menu, remove_item_input)
availability = check_item(initial_menu, check_item_input)

print(f"Updated menu: {initial_menu}")
print(availability)