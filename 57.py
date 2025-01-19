def find_and_replace(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        contents = file.read()
    contents = contents.replace(old_word, new_word)
    with open(file_path, 'w') as file:
        file.write(contents)

# Example usage
find_and_replace('example.txt', 'old', 'new')  # Replace with your file path and words
