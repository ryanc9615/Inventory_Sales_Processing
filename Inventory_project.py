product_data = {}

products_sold = []

total_revenue = 0
total_costs = 0

while True: 
    product_name = input("Please enter your product: ").strip()

    if not product_name:
        print("Product name cannot be empty. Please try again.")
        continue

    while True: 
        try:
            cost_price = float(input("Please enter your cost price: "))
            break
        except ValueError:
            print("Invalid cost price. Please enter a numeric value.")

    while True: 
        try:
            quantity = int(input("Please enter your product quantities: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
    
    while True: 
        try:
            sales_price = float(input("Please enter your sales price: "))
            break
        except ValueError:
            print("Invalid sales price. Please enter a numeric value.")
    
    if product_name in product_data:
        print(f"Warning: '{product_name}' already exists. Values will be updated.")

    product_data[product_name] = {
        "cost price": cost_price,
        "quantity": quantity, 
        "sale_price": sales_price
    }

    enter_more = input("Type 'no' if you have no more products to enter, or press Enter to continue: ").strip().lower()
    if enter_more == "no":
        break

print(("All products have been recoreded successfully!"))

print(product_data)

while True:
    sale_product = input("Enter product name to record a sale (or 'exit' to finish):").strip()

    if sale_product.lower() == "exit":
        break

    if sale_product not in product_data:
        print(f"Product '{sale_product}' not found in inventory.")
        continue

    while True: 
        try:
            sale_quantity = int(input("Enter quantity sold: "))
            if sale_quantity <= 0:
                print("Quantity must be positive.")
                continue
            if sale_quantity > product_data[sale_product]["quantity"]:
                print(f"Error: Only {product_data[sale_product]['quantity']} units available.")
                continue
            break 
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
    
    sale_price_total = sale_quantity * product_data[sale_product]["sale_price"]
    cost_price_total = sale_quantity * product_data[sale_product]["cost_price"]
    profit = sale_price_total - cost_price_total

    product_data[sale_product]["quantity"] -= sale_quantity

    products_sold.append({
        "product": sale_product,
        "quantity": sale_quantity,
        "sale_price_total": sale_price_total,
        "cost_price_total": cost_price_total,
        "profit": profit
    })

    total_revenue += sale_price_total
    total_costs += cost_price_total

    print(f"\nSale recorded successfully!")
    print(f"Sale total: ${sale_price_total:.2f}")
    print(f"Profit: ${profit:.2f}")
    print(f"Remaining quantity: {product_data[sale_product]['quantity']}")

print("\nFinal Sales Summary:")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Total Costs: ${total_costs:.2f}")
print(f"Total Profit: ${total_revenue - total_costs:.2f}")


