def word_count(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    words = contents.split()
    return len(words)

# Example usage
file_path = 'example.txt'  # Replace with your file path
print(f"Number of words: {word_count(file_path)}")
