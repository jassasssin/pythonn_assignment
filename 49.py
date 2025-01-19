def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 18
print(gcd(num1, num2))
