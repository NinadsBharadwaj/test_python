def main():
    n=int(input(" enter the value of x"))
    if even(n):
        print("even")
    else :
        print("odd")

def even(x):
    if x%2==0 :
        return True
    else :
        return False
    
main()
