#Wap using is_prime(), display all prime numbers between two integers start and end

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True 

start=int(input("Enter a start number: "))
end=int(input("Enter a end number: "))
for i in range(start,end+1):
    if is_prime(i):
        print(i)
        