def find():
    cp = float(input("Enter the Cost Price (CP): "))
    sp = float(input("Enter the Selling Price (SP): "))

    if sp > cp:
        print("Profit")
    elif cp > sp:
        print("Loss ")
    else:
        print("Neither profit nor loss.")
        
find()