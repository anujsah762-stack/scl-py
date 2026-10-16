def arm(n):
    s=0
    while n>0:
        r=n%10
        s=s+r**3
        n=n//10
    return s

x=int(input("Enter a number: "))
if x==arm(x):
    print("The number is an Armstrong number")  
else:
    print("The number is not an Armstrong number")