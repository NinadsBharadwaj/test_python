#first take input from user in camel case.
#then pass the value to snake_case
#then place an underscore before capital letter
#then convert eveything to lowercase

def main():
    camelCase=input("camelCase:")
    print("snake_case:",end="")
    snake_case(camelCase)

def snake_case(x):
    for letter in x:
        if letter.isupper():
            print("_"+letter.lower(),end="") #do not use comma here as it adds an extra space

        else:
            print(letter,end="")

main()




















