#Shopping Bill Calculator

products = {
    "Milk": 250,
    "Bread": 150,
    "Eggs": 400,
    "Rice": 1200
}

def calculate_discount(total):
    if total >= 5000:
        return total * 0.10
    else:
        return 0

total = 0

print("Available Products & Prices:")
for item, price in products.items():
    print(f"- {item}: Rs. {price}")

print("\n--- Shopping Cart (Type 'done' to finish) ---")
while True:
    selected_item = input("Enter product name: ").capitalize()
    
    if selected_item == "Done":
        break
    
    if selected_item in products:
        try:
            qty = int(input(f"Enter quantity for {selected_item}: "))
            if qty > 0:
                total += products[selected_item] * qty
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number for quantity.")
    else:
        print("Item not found in products list.")

discount = calculate_discount(total)
final_bill = total - discount

print("\n--- Bill Summary ---")
print(f"Original Bill: Rs. {total}")
print(f"Discount: Rs. {discount}")
print(f"Final Bill: Rs. {final_bill}")