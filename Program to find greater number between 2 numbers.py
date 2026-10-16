def great(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = great(x, y)
print("The greater number is:", z)