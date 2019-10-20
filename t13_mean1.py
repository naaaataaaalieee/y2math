# Find the mean of n numbers
n = int(input("Please input number of numbers to calculate mean"))
numbers = []
total = 0
for i in range(n):
  numbers.append(float(input("Please input the next number")))
for number in numbers:
  total = number + total
print(numbers)
print(total / n)
