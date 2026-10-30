
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    units = int(input("Enter electricity units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill += 50  # Fixed charge
    bill += bill * 0.05  # 5% surcharge

    if units < 50:
        bill -= 20  # Rebate

    bills.append(bill)
    print("Monthly Bill: Rs.", round(bill, 2))

print("\n--- BILL COMPARISON ---")

for i in range(1, n):
    increase = bills[i] - bills[i - 1]
    print("Month", i + 1, "Increase: Rs.", round(increase, 2))

    if increase > bills[i - 1] * 0.20:
        print("Unusual increase detected!")
