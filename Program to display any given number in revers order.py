def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    print("The reverse of the number is:",s)

x=int(input("Enter a number: "))
rev(x)