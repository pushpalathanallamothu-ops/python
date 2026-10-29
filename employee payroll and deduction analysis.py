
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

net_salary = gross - deduction

print("\n--- SALARY STATEMENT ---")
print("Employee Name:", name)
print("Basic Pay:", basic)
print("Allowances:", allowances)
print("Overtime:", overtime)
print("Incentives:", incentives)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net_salary)
