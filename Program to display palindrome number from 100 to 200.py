def pali():
    for i in range(100,201):
        x=i
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(i==rev):
            print(rev,end=" ")

pali()