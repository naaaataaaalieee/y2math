# Find elements common to a and b
a = [1, 3, 9, 2, 5, 18, 3, 9, 2]
b = [0, 2, 9, 2]

# Consider this approach where for each element in a,
# we iterate through b to check if the element exists

for i in range (len(a)):
    for j in range (len(b)):
        if a[i] == b[j]:
            # Do something


# Consider another approach where we sort both arrays first
a.sort()
b.sort()

# Now, we get the lower bound of where we should start searching
lower_bound = max(a[0], b[0])
upper_bound = min(a[len(a)-1], b[len(b)-1])
'''
Why does this work?
Arrays after sorted will look like:
a = [1, 2, 2, 3, 3, 5, 9, 9, 18]
b = [0, 2, 2, 9]

lower_bound = max(a[0], b[0]) = max(1, 0) = 1
=> 0 will never be in a.

upper_bound = min(a[len(a)-1], b[len(b)-1]) = min(18, 9) = 9
=> Likewise, we can never find 18 in b

Hence, why not we just search from 1 to 9?
'''

# YOUR TURN: Modify the FOR loop above
