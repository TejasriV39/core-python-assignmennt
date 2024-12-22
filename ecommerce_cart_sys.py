def calculate_total_price(cart_items):
    if not cart_items:
        return "Cart is empty."
    
    total_price = sum(cart_items.values())
    
    if len(cart_items) > 5:
        total_price *= 0.9  # Applying 10% discount
    
    return total_price

# input
cart_items = {}
num_items = int(input("Enter the number of items in the cart: "))
for _ in range(num_items):
    item_name = input("Enter item name: ")
    item_price = float(input(f"Enter price for {item_name}: "))
    cart_items[item_name] = item_price

total_price = calculate_total_price(cart_items)
print(f"Total Price: {total_price}")