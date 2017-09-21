#This program gives prime number in a range
count=0;
lower=int(input("Enter Lower end \n"))
upper=int(input("Enter Upper end \n \n \n"))
for t in range(lower,upper+1):
    if t>1:
        for p in range(2,int(t/2)):
            if (t%p)==0:
                break
        else:
            print(t)




