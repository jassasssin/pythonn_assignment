def count_vowels(s):
    if not s:
        return 0
    vowels = 'aeiouAEIOU'
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

# Example usage
string = "Hello World"
print(f"Number of vowels in '{string}': {count_vowels(string)}")
