def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

# Example usage
file_path = 'example.txt'  # Replace with your file path
print(f"Number of lines: {count_lines(file_path)}")
