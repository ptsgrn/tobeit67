import math
prices = {
    "shrimp sour soup": 80,
    "mixed vegetables sour soup": 60,
    "papaya sour soup": 55,
    "snapper fish sour soup": 100,
    "cha om shrimp sour soup": 100
}

stop = False
price = 0
count = 0
while not stop:
    order = input()
    if order == 'stop':
        stop = True
        break
    price = price + prices[order]
    count = count + 1
print("Original Price", price, "baht")
discount = 0
if count >= 3 and price >= 200:
    discount = price * 0.15
print("Discount", int(discount), "baht")
print("Total", math.floor(price - discount), "baht")
