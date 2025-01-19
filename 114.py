# List comprehension vs Generator expression
large_data = range(1000000)

# List comprehension
list_comprehension = [x * 2 for x in large_data]
print(f"List comprehension created a list of length: {len(list_comprehension)}")

# Generator expression
generator_expression = (x * 2 for x in large_data)
print(f"Generator expression created a generator object.")
print(f"First value from generator: {next(generator_expression)}")
