def check (a):
    if a > 0:
        print(a, "is Positive")
    elif a < 0:
        print(a, "is Negative")
    else:
        print(a, "is Zero")

x = int(input("Enter a number: "))
check(x)