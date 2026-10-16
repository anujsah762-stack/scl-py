def prime():
    for n in range(10, 101):
        c=0
        for i in range(1, n+1):
            if n%i==0:
                c+=1
        if c==2:
            print(n,end=" ")    

prime()