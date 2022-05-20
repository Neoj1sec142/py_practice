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

def getPrice(prod, amt):
    priceData = {
        'Biscuit':3,
        'Chicken':5,
        'Egg':1,
        'Fish':3,
        'Coke':2,
        'Bread':2,
        'Apple':3,
        'Onion':3
    }
    subtotal = priceData[prod] * amt
    print(prod + '$' + str(priceData[prod]) + 'x' +
    str(amt) + '=' + str(subtotal))
    return subtotal

def getDiscount(billAmt, membership):
    discount = 0
    if billAmt >= 25:
        if membership == 'Gold':
            billAmt = billAmt * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmt = billAmt * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmt = billAmt * 0.95
            discount = 5
        print(str(discount) + '% off for' + membership + '' + 'membership on total amount: $' + str(billAmt))
    else: 
        print("No discount on items under 25")
    return billAmt
getDiscount(30, 'Silver')