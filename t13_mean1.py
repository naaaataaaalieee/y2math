# Find the mean of n numbers

n = int(input("Enter number of numbers: "))
numbers = []
total = 0
for i in range(n):
  numbers.append(float(input("Enter number: ")))
for number in numbers:
  total = total + number
print(numbers)
print(total / n)
