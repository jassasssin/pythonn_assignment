def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))
