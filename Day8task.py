#task1:
sum=0
num=int(input("Enter the  number:"))
while num>0:
    sum+=num
    num=int(input("Enter the  number:"))
print(sum)

#task2

numbers = [7, 0, 8, -1, 10]
i = 0
positive = []
negative = []
while i < len(numbers):
    if numbers[i] > 0:
        positive.append(numbers[i])
    else:
        negative.append(numbers[i])
    i += 1
print("positive numbers:", positive)
print("negative numbers:", negative)
