def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Example usage
original_dict = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(original_dict))
