# Task 1
n = 0
while True:
    n += 1
    print(n, "Ragavi")
    if n == 5:
        break

# Task 2
list1 = []
list2 = []
i = 0

while i <= 100:
    if i % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
    i += 1

print("Even numbers:", list1)
print("Odd numbers:", list2)
