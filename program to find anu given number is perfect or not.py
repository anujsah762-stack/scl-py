def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s

x=int(input("Enter a number: "))
if x==perfect(x):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")