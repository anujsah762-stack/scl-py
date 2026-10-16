def factorial(n):
    f=1
    for i in range(1, n + 1):
        f = f * i
    print("The factorial of", n, "is", f)

x = int(input("Enter a number: "))
factorial(x)