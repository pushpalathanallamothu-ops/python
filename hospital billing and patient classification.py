
name = input("Enter patient name: ")
consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))
age = int(input("Enter patient age: "))

if consultation < 0 or diagnostic < 0 or treatment < 0 or age < 0:
    print("Invalid billing details!")
else:
    total = consultation + diagnostic + treatment

    if age >= 60:
        discount = total * 0.20
    elif total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    if final_bill <= 2000:
        category = "Low Payment"
    elif final_bill <= 10000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("\n--- HOSPITAL BILL ---")
    print("Patient:", name)
    print("Total Charges: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)
    print("Payment Category:", category)
