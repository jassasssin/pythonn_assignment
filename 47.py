def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference

# Example usage
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_operations(set_a, set_b))
