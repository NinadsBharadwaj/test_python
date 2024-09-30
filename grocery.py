grocery={}

while True:
    try :
        x=input()
        if x in grocery:
            grocery[x]+=1
        else:
            grocery[x]=1

    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key],key)
            break    
