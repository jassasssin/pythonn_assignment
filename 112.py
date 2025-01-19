# Using a lambda function inside map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled Numbers: {doubled_numbers}")
