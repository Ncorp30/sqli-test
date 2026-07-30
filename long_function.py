def process_order(order):
    if not isinstance(order, dict):
        return "Invalid order"

    # Validate customer
    customer = order.get("customer")
    if not isinstance(customer, dict):
        return "Invalid customer"

    # Validate address
    address = customer.get("address")
    if address is None:
        return "Missing address"

    # Calculate pricing
    price = 0

    item_price_multipliers = {
        "book": 0.9,
        "electronics": 0.8,
    }

    for item in order.get("items", []):
        if not isinstance(item, dict):
            continue
        multiplier = item_price_multipliers.get(item.get("type"), 1)
        price += item.get("price", 0) * multiplier

    # Apply discounts
    if order.get("discount"):
        price -= price * 0.1

    # Calculate tax
    tax = price * 0.18
    final_price = price + tax

    # Create invoice
    invoice = {
        "customer": customer.get("name"),
        "address": address,
        "amount": final_price
    }

    # Save invoice
    print("Saving invoice...")
    print(invoice)

    # Send notification
    print("Sending email...")
    
    return invoice
