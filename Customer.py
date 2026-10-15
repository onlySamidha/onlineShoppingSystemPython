# Name: Samidha Mote 
# Roll no.: 2643
#
# Customer class represents a customer and stores customer details such as customer id, customer name, email, phone and address.
# The data members are declared as private to implement encapsulation. they are accessed using getter and setter methods.
# Class also provides methods such as login(), register(), and placeOrder*() to perform customer related operations.
class Customer:
    def __init__(self):
        self.customerid = None
        self.name = None
        self.email = None
        self.phone = None
        self.address = None

    # Sets the customer id
    def setCustomerid(self, customerid):
        self.customerid = customerid
    # Returns the customer id
    def getCustomerid(self):
        return self.customerid

    # Sets the customer name
    def setName(self, name):
        self.name = name
    # Returns the customer name
    def getName(self):
        return self.name

    # Sets customer email address
    def setEmail(self, email):
        self.email = email
    # Return the customer email address
    def getEmail(self):
        return self.email

    #Sets customer phone number
    def setPhone(self, phone):
        self.phone = phone
    # Returns customer phone number
    def getPhone(self):
        return self.phone

    # Sets customer address
    def setAddress(self, address):
        self.address = address
    # Returns customer address
    def getAddress(self):
        return self.address

    # Logs customer into the system
    def login(self):
        print("Customer has logged in.")

    # Registers new customer
    def registerCustomer(self):
        print("Customer has registered.")

    # Places an order for the customer
    def placeOrder(self):
        print("Order has been placed.")
