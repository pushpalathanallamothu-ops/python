
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
target = float(input("Enter required attendance percentage: "))

percentage = (attended / total) * 100

print("Current Attendance:", round(percentage, 2), "%")

if percentage >= target:
    print("You are already eligible.")
else:
    classes = 0
    while (attended + classes) / (total + classes) * 100 < target:
        classes += 1

    print("Minimum consecutive classes to attend:", classes)
    print("Attendance after recovery:",
          round((attended + classes) / (total + classes) * 100, 2), "%")
