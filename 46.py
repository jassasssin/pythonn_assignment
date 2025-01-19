def frequency_of_elements(lst):
    frequency = {}
    for element in lst:
        frequency[element] = frequency.get(element, 0) + 1
    return frequency

# Example usage
elements = [1, 2, 2, 3, 3, 3, 4]
print(frequency_of_elements(elements))
