def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Example usage
string = "Racecar"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")
