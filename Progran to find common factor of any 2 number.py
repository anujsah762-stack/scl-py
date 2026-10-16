def common_factor(a, b):
    if a>b:
        c = a
    else:
        c = b
    for i in range(1, c + 1):
        if a % i == 0 and b % i == 0:
            print(i)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
common_factor(x, y)