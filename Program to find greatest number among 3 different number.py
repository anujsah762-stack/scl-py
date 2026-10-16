def greatest(a,b,c):
    if a >= b and a >= c:
        print(a,"is the greatest number")
    elif b >= a and b >= c:
        print(b,"is the greatest number")
    else:
        print(c,"is the greatest number")

x = int(input("Enter first number: "))
y = int(input("Enter second number: ")) 
z = int(input("Enter third number: "))
greatest(x,y,z)