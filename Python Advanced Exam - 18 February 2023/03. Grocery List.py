def shop_from_grocery_list(budget, grocery_list, *products):
    purchased_products = set()
    total_cost = 0

    for product, price in products:
        if price > budget:
            break
        if product in grocery_list and product not in purchased_products and budget >= price:
            budget -= price
            total_cost += price
            purchased_products.add(product)

    if len(purchased_products) == len(grocery_list):
        budget_left = budget
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        missing_products = set(grocery_list) - purchased_products
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))




