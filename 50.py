def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
num1 = 4
num2 = 5
print(lcm(num1, num2))
