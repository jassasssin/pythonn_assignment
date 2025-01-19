import statistics

# Example list of numbers
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Compute mean, median, and mode
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)

# Display results
print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")
