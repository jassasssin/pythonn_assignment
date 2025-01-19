str = input("Enter a string: ")

str = str.lower()
c=input("Enter a character: ")
b=input("Enter the replacing value: ")
c=c.lower()
for i in str:
    if i == c:
        str=str.replace(i,b)
print(str)