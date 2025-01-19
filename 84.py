def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')

# Example usage
user_input = input("Enter a line to append to the file: ")
append_to_file('output.txt', user_input)  # Replace with your file path
