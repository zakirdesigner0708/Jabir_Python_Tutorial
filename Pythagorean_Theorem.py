import math

# Take input for the coordinates of the first point
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# Take input for the coordinates of the second point
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Display the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")