def div(a):
    if a % 3 == 0 and a % 5 == 0:
        print(a," is divisible by both 3 and 5.")
    elif a % 3 == 0:
        print(a," is divisible by 3.")
    elif a % 5 == 0:
        print(a," is divisible by 5.")
    else:
        print(a," is not divisible by either 3 or 5.")

x = int(input("Enter a number: "))
div(x)