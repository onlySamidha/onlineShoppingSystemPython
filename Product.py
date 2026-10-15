# Name: Samidha Mote 
# Roll no.: 2643
#
# Product class represents the products available in the online shopping management system.
# It stores product details such as product id, name, price and stock.
# It also provides methods to update stock and display product information.
class Product:
    def __init__(self):
        self.productId = None
        self.name = None
        self.price = None
        self.stock = None

    # Sets the product id
    def setProductId(self, productId):
        self.productId = productId
    # Returns the product id
    def getproductId(self):
        return self.productId

    # Sets the product name
    def setName(self, name):
        self.name = name
    # Returns the product name
    def getName(self):
        return self.name

    # Sets the product price
    def setPrice(self, price):
        self.price = price
    # Returns the product price
    def getprice(self):
        return self.price

    # Sets the available stock of the product
    def setStock(self, stock):
        self.stock = stock
    # Returns the available stock of the product
    def getstock(self):
        return self.stock

    # Updates the stock of the product
    def updateStock(self):
        print("Stock updated")

    # Displays the detils of the product
    def displayDetails(self):
        print("displaying product details")
