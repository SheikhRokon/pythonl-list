# n স্ংখ্যার মৌলিিক সংখ্যা বেড় করাা

a = int(input("Enter your fast postive number: "))
b = int(input("Enter your last postive number: "))



for x in range(a,b+1):
    if x>1:

        for x in range(2,x):
            if x%1==0:
                break 
            else:
                print(x)  

