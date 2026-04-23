print("📘 Student Result System")
name = input("Enter student name: ")
try:
    maths = int(input("Enter Maths marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))
except:
    print("Invalid input! Please enter numbers only.")
    exit()

total = maths + physics + chemistry
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

if maths < 33 or physics < 33 or chemistry < 33:
    result = "Fail"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)