# Name: Samidha Mote 
# Roll no.: 2643
#
# Cart class represents the shopping cart of a customer.
# It contains cart details and methods to manage the cart
class Cart:
    def __init__(self):
        self.cartId = None
        self.createDate = None

    # sets the cart id  
    def setCartId(self, cartId):
        self.cartId = cartId
    # Returns the cart id  
    def getCartId(self):
        return self.cartId

    # Sets the cart creation date 
    def setCreateDate(self, createDate):
        self.createDate = createDate
    # Return the cart creation date 
    def getCreateDate(self):
        return self.createDate

    # Adds item to the cart
    def addItem(self):
        print("Item added")

    # Removes item from the cart
    def removeItem(self):
        print("Item removed")

    #Displays the items present in the cart
    def viewCart(self):
        print("viewing")
