import math

# Get user input
number = float(input("Enter a number: "))

# Compute square root, floor, and ceiling
square_root = math.sqrt(number)
floor_value = math.floor(number)
ceiling_value = math.ceil(number)

# Display results
print(f"Square root: {square_root}")
print(f"Floor: {floor_value}")
print(f"Ceiling: {ceiling_value}")
