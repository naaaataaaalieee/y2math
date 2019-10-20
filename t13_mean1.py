# Find the mean of n numbers
import random

n = 10
numbers = []

for i in range(n):
  numbers.append(random.randint(1,100)) # between 1 to 100 inclusive

total = 0
for number in numbers:
  total += number
print(numbers)
print(total / n)
