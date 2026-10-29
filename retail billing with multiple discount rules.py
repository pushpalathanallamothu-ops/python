
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/other): ").lower()

    amount = price * qty

    if category == "food":
        tax = amount * 0.05
    else:
        tax = amount * 0.18

    discount = amount * 0.10 if amount >= 1000 else 0
    discount = min(discount, 500)

    final = amount + tax - discount
    total += final

    print("\nProduct:", name)
    print("Amount: Rs.", round(amount, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Price: Rs.", round(final, 2))

print("\nTotal Bill: Rs.", round(total, 2))
