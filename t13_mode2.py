# Find mode(s) of n numbers

A = [19, 18, 46, 18, 18, 19, 19]

modes = {}
for num in A:
  if num not in modes:
    modes[num] = 1
  else:
    modes[num] += 1
print(modes)

highest = max(modes.values())
print(highest)

print("Mode: ", end='')
for key, value in modes.items():
  if value == highest:
    print(key, end=' ')
