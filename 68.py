def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Example usage
base = 2
exp = 3
print(f"{base} raised to the power of {exp}: {power(base, exp)}")
