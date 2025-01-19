def search_in_file(file_path, substring):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    matching_lines = [line for line in lines if substring in line]
    return matching_lines

# Example usage
file_path = 'example.txt'  # Replace with your file path
substring = 'search_term'  # Replace with the substring to search for
print(f"Lines containing '{substring}':")
for line in search_in_file(file_path, substring):
    print(line, end='')
