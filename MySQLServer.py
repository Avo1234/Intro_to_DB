def calculate_price(price, tax):
    total = price + (price * tax)
    return total


print(calculate_price(100, 0.05))