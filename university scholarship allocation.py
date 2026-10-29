
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if (marks >= 75 and s1 >= 40 and s2 >= 40
            and attendance >= 75 and income <= 200000):
        students.append((name, marks, attendance))
        
students.sort(key=lambda x: (-x[1], -x[2], x[0]))

print("\n--- SCHOLARSHIP RANK LIST ---")

if len(students) == 0:
    print("No eligible students")
else:
    for i, student in enumerate(students, 1):
        print(i, student[0],
              "Marks:", student[1],
              "Attendance:", student[2])
