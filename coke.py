#create a variable
#loop which prints the value if  change >0
#print amount due\
#ask user to inbput coin
#check if its 5,10,25
#subtract value from amount due
#print


amt_due=50
while amt_due>0:
    print("Amount_due:",amt_due)
    coin=int(input("Enter coin:"))
    if coin==5 or coin==10 or coin==25:
        amt_due -= coin
balance=abs(amt_due)
print("Change:",balance)

