
n = int(input("Enter number of invoice records: "))

for i in range(n):
    record = input("Enter record (code,quantity,amount): ")

    parts = record.split(",")

    if len(parts) != 3:
        print("Malformed record!")
        continue

    code = parts[0].strip()

    try:
        quantity = int(parts[1])
        amount = float(parts[2])

        if code == "" or quantity <= 0 or amount < 0:
            print("Malformed record!")
        else:
            print("Product Code:", code)
            print("Quantity:", quantity)
            print("Amount: Rs.", amount)

    except ValueError:
        print("Malformed record!")

