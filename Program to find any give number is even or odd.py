def check(a):
    if a % 2 == 0:
        print(a, "is Even")
    else:
        print(a, "is Odd")

x = int(input("Enter a number: "))
check(x)