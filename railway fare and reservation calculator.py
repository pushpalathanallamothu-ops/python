
n = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))

for i in range(n):
    age = int(input("Enter passenger age: "))
    cls = input("Enter class (sleeper/ac): ").lower()

    rate = 1 if cls == "sleeper" else 2
    fare = distance * rate

    if distance > 500:
        fare += 100
    elif distance > 200:
        fare += 50

    if age < 12:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.7

    fare += 50  # Reservation fee

    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel == "yes":
        fare *= 0.5  # 50% cancellation penalty

    print("Passenger", i + 1, "Fare: Rs.", round(fare, 2))
