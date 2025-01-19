import random

def select_random_element(elements):
    return random.choice(elements)

# Example usage
my_list = [1, 2, 3, 4, 5]
random_element = select_random_element(my_list)
print(f"Randomly selected element: {random_element}")
