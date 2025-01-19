def second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in lst:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second

# Example usage
unique_numbers = [10, 20, 4, 45, 99]
print(second_largest(unique_numbers))
