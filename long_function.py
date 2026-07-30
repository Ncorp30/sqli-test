def process_order(order):
    # Validate customer
    if order["customer"] is None:
        return "Invalid customer"

    customer = order["customer"]

    # Validate address
    if customer["address"] is None:
        return "Missing address"

    address = customer["address"]

    # Calculate pricing
    price = 0

    for item in order["items"]:
        if item["type"] == "book":
            price += item["price"] * 0.9
        elif item["type"] == "electronics":
            price += item["price"] * 0.8
        else:
            price += item["price"]

    # Apply discounts
    if order["discount"]:
        price -= price * 0.1

    # Calculate tax
    tax = price * 0.18
    final_price = price + tax

    # Create invoice
    invoice = {
        "customer": customer["name"],
        "address": address,
        "amount": final_price
    }

    # Save invoice
    print("Saving invoice...")
    print(invoice)

    # Send notification
    print("Sending email...")
    
    return invoice
