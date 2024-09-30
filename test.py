x=input("Input:")
print("output:",end="")
for letter in x:
    if not letter.lower() in ['a','e','i','u','o']:
        print(letter.lower(),end="")