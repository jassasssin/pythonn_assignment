def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        contents = source_file.read()
    with open(destination_path, 'w') as dest_file:
        dest_file.write(contents)

# Example usage
copy_file('source.txt', 'destination.txt')  # Replace with your file paths
