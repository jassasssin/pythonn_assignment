def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

# Example usage
file_path = 'example.txt'  # Replace with your file path
print(read_file(file_path))
