menu = {
    "pizza": 22.6,
    "burger": 12.2,
    "lays": 10.1,
    "biriyani": 8.9,
    "chicken": 5.5
}

cart = []
total = 0.0

print("-------------Menu-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value}")
print("------------------------------")

while True:
    food = input("enter your items(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found in menu!")

for food in cart:
    total += menu.get(food)
    print(food, end=" - ")

print()
print(total)
