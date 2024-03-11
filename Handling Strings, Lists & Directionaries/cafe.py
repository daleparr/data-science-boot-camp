menu = ["soup", "sandwich", "pancakes", "coffee" ]

stock = {
    'soup': 100,
    'sandwich': 200,
    'pancakes': 50,
    'coffee': 30,
}

price = {
    'soup': 2.5,
    'sandwich': 2.0,
    'pancakes': 5.0,
    'coffee': 3.5,
}

total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

print(f"The total stock worth of the cafe is: ${total_stock_worth:.2f}")