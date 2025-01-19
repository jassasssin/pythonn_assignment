def read_file_with_exceptions(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found. Please check the file path."

# Example usage
file_path = 'example.txt'  # Replace with your file path
print(read_file_with_exceptions(file_path))
