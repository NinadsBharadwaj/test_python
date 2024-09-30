#take input from user
#check if input has vowel so create a loop
#delete vowel and print in lower case

answer=input("Input:")
print("Outpur is:",end="")
for letter in answer:
    if not letter   in ['a','e','i','o','u']:
        print(letter,end="")
   