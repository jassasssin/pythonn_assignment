def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Example usage
user_input = input("Enter a number: ")
print(convert_to_int(user_input))
