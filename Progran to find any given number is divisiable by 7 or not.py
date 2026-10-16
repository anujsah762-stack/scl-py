def div(a):
    if a % 7 == 0:
        print(a,"is divisible by 7")
    else:
        print(a,"is not divisible by 7")

x = int(input("Enter a number: "))
div(x)