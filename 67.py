def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage
n = 6
print(f"The {n}th Fibonacci number: {fib(n)}")
