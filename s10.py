def series ():
    n=7
    for i in range(1,11):
        print(n,end=" ")
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

series()