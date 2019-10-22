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


# Alternative solutions    
# Contributed by 19Y2J BEN SZE HE YU
A = [1, 2, 3, 4, 5, 5] 
n = len(A) 
  
data = Counter(A) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == n: 
    print("No mode found")
else: 
    print("Mode is / are: " + ', '.join(map(str, mode))
          
          
          
          
