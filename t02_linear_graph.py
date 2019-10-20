'''
Linear graph: Y = mX + c
'''

# Get user inputs for gradient and y-intercept
m = int(input("Enter the gradient of the line: "))
c = int(input("Enter the y-intercept of the line: "))

# Show equation to user
print("Your equation is:", "y = "+str(m)+"x + "+str(c))

# Concept: List iteration
# Generate x values for plotting
# Generally, we use at least 5 x-values for a best fit line
x_values = [x for x in range (-3, 7)]

# Get corresponding y values
y_values = [m*x_values[i] + c for i in range (len(x_values))]

# Show data to user
print("We are plotting:")
print("x:", x_values)
print("y:", y_values)

# Define the max and min y boundaries and start plotting for each y
# min_y and max_y corresponds to the min and max 'window' height
min_y = min(y_values)
max_y = max(y_values)

# Define the max and min x boundaries and start plotting for each x
# min_x and max_x corresponds to the min and max 'window' length
min_x = min(x_values)
max_x = max(x_values)

# Set the coords height and length boundaries (matrix)
if min_x >=0:
    x_length = abs(max_x)
else:
    x_length = abs(max_x) + abs(min_x)


if min_y >= 0:
    y_height = abs(max_y)
else:
    y_height = abs(max_y) + abs(min_y)

SIZE = max(y_height, x_length)+1
BUFFER = 1
coords = [[" "*2 for i in range (SIZE+BUFFER)] for i in range (SIZE+BUFFER)]

# Draw the axes
# x-axis:
if min_y >= 0:
    ZERO_LINE = SIZE-1
    for i in range (SIZE+BUFFER):
        if i == SIZE+BUFFER-1:
            coords[ZERO_LINE][i] = "> x"
        else:
            coords[ZERO_LINE][i] = "_ "
else:
    for i in range (SIZE+BUFFER):
        ZERO_LINE = abs(max_y)
        if i == SIZE+BUFFER-1:
            coords[ZERO_LINE][i] = "> x "
        else:
            coords[ZERO_LINE][i] = "_ "

# y-axis:
if min_x >= 0:
    temp_x = 0
    for i in range (SIZE+BUFFER):
        if i == 0:
            coords[i][0] = "^ "
        else:
            coords[i][0] = "| "
else:
    temp_x = abs(min_x)
    for i in range (SIZE+BUFFER):
        if i == 0:
            coords[i][abs(min_x)] = "^ "
        else:
            coords[i][abs(min_x)] = "| "
print(" "*2*(temp_x-1)+"y")

# Add in coordinates
for i in range (len(y_values)):
    coords[abs(y_values[i]-ZERO_LINE)][x_values[i]+abs(min_x)] = "* "
    
# Display graph
for y in range (len(coords)):
    for x in range (len(coords[y])):
        print(coords[y][x], end="")
    print()


