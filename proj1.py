## First Project on CodingX App for Python Supermarket Cashier ##

#function to enter products:
def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit:")
        if details in ['a', 'A', "add", "ADD", 'Add']:
            product = input("Enter product:")
            quantity = int(input("Enter quantity:"))
            buyingData.update({product:quantity})
        elif details in ['q', 'Q', 'quit', 'QUIT', 'Quit']:
            enterDetails = False
        else:
            print("Please select correct option.")
    return buyingData

