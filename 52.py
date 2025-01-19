def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
user_input = input("Enter a string to write to the file: ")
write_to_file('output.txt', user_input)
