
budget = float(input("Enter travel budget in INR: "))
rate = float(input("Enter exchange rate (1 foreign unit in INR): "))
fee = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expense categories: "))
expenses = []

for i in range(n):
    name = input("Enter expense category: ")
    amount = float(input("Enter expense in foreign currency: "))

    cost = amount * rate
    cost += cost * fee / 100
    expenses.append((name, cost))

total = sum(x[1] for x in expenses)

print("\n--- TRAVEL BUDGET REPORT ---")
for name, cost in expenses:
    print(name, ": Rs.", round(cost, 2))

print("Total Spending: Rs.", round(total, 2))
print("Budget: Rs.", budget)

if total > budget:
    print("Budget Exceeded!")
else:
    print("Within Budget")

largest = max(expenses, key=lambda x: x[1])
print("Largest Expense:", largest[0])
