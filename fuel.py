while True:
    fuel=input("fraction :")
    try:
        numer,denom=fuel.split("/")
        num1=int(numer)
        denom1=int(denom)
        f=num1/denom1
        break
    except(ValueError,ZeroDivisionError):
        pass
per=f*100
if(per==100):
    print("F")
elif(per==0):
    print("E")
else:
    print(per,"%")
