word = input("Enter a name: ")
count = 0
for i in word:
    if i in "aeiou":
        count += 1
print(count)