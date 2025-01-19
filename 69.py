def sum_of_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_of_list(lst[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
print(f"Sum of the list: {sum_of_list(numbers)}")
