from functools import reduce

# Using filter to filter out even numbers and reduce to sum the filtered numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
sum_of_odds = reduce(lambda x, y: x + y, filtered_numbers)

print(f"Filtered Odd Numbers: {filtered_numbers}")
print(f"Sum of Odd Numbers: {sum_of_odds}")
