#Write a function is_prime(num) that checks if a number is prime.

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num=int(input("Enter a number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
    