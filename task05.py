#Restaurant Ordering System

menu = {
    "Biryani": 350,
    "Karahi": 1200,
    "Naan": 50,
    "Tea": 100
}

def calculate_item_total(price, quantity):
    return price * quantity

total = 0
order_summary = {}  # Challenge: separate dictionary for items and quantities

print("--- Restaurant Menu ---")
for item, price in menu.items():
    print(f"- {item}: Rs. {price}")
print("-----------------------")

while True:
    item = input("Enter item name or done: ").title()

    if item == "Done":
        break

    if item in menu:
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if quantity > 0:
                item_total = calculate_item_total(menu[item], quantity)
                total += item_total
                
                # Store ordered items in dictionary
                if item in order_summary:
                    order_summary[item] += quantity
                else:
                    order_summary[item] = quantity
                print(f"Added {quantity} x {item} (Rs. {item_total})")
            else:
                print("Quantity must be at least 1.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Error: Item does not exist in the menu.")

print("\n--- Ordered Items ---")
for item, qty in order_summary.items():
    print(f"{item}: {qty}")
print("Total bill: Rs.", total)