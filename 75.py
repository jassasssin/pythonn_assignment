def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Example usage
num1 = 48
num2 = 18
print(f"GCD of {num1} and {num2}: {gcd_recursive(num1, num2)}")
