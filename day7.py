# Task 1: Login System

string1 = "username"
string2 = "email"
string3 = "password"

m1 = input("Enter the username: ")
m2 = input("Enter the email: ")
m3 = input("Enter the password: ")

if m1 == string1 and m2 == string2 and m3 == string3:
    print("Login successfully")
else:
    print("Incorrect")

# Task 2: Number Digit Checker

n = int(input("Enter the number: "))

if n <= 9:
    print("Single digit number")
elif n <= 99:
    print("Double digit number")
elif n <= 999:
    print("Three digit number")
elif n <= 9999:
    print("Four digit number")
else:
    print("Nothing to print")

# Task 3: Marks and Grade Calculation

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))
mark4 = int(input("Enter mark 4: "))
mark5 = int(input("Enter mark 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
print("Total =", total)

per = total / 5
print("Percentage =", per)

if per < 25:
    print("Grade is F")
elif per >= 25 and per < 45:
    print("Grade is E")
elif per >= 45 and per < 50:
    print("Grade is D")
elif per >= 50 and per < 60:
    print("Grade is C")
elif per >= 60 and per < 80:
    print("Grade is B")
elif per >= 80:
    print("Grade is A")
else:
    print("Nothing")

# Task 4: Attendance Percentage

a = int(input("Number of classes held: "))
b = int(input("Number of classes attended: "))

per = (b / a) * 100
print("Attendance Percentage =", per)

if per >= 75:
    print("Student is allowed to write exam")
else:
    print("Not allowed to write exam")
