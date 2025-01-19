def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    return longest_word

# Example usage
file_path = 'example.txt'  # Replace with your file path
print(f"Longest word: {find_longest_word(file_path)}")
