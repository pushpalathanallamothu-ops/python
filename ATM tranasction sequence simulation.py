
balance = float(input("Enter initial balance: "))
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")
    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")
    elif choice == 1:
        balance += amount
        transactions.append("Deposit: Rs. " + str(amount))
        print("Deposit successful")
    elif choice == 2:
        if amount > 10000:
            print("Withdrawal limit exceeded!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions.append("Withdrawal: Rs. " + str(amount))
            print("Withdrawal successful")
    else:
        print("Invalid choice!")

print("\n--- ATM SUMMARY ---")
for t in transactions:
    print(t)

print("Final Balance: Rs.", balance)
print("Successful Transactions:", len(transactions))
