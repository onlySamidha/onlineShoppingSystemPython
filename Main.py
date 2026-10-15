# Name: Samidha Mote 
# Roll no.: 2643
#
# Main class is te entry point of the Online Shopping Management system.
# This class demonstratea the working of the project by creating objects of different classes such as Customer, Products and shipment. 
# It also demonstrates encapsulation using getter and setter methods
from Customer import Customer
from Product import Product
from Cart import Cart
from Order import Order
from Payment import Payment
from Shipment import Shipment

# The main() method is the entry point of the program.
# It creates objects, initializes data using setter methods.
# Retrives data using getter methods and invokes methods to perform shopping operations.
def main():

    c = Customer()
    c.setCustomerid(10)
    c.setName("Samidha")
    c.setEmail("samidhamote04@gmail.com")

    p = Product()
    p.setProductId(1)
    p.setName("laptop")
    p.setPrice(67000)

    cart = Cart()
    o = Order()
    pay = Payment()
    s = Shipment()

    print("Customer:" + c.getName())
    print("Product:" + p.getName())
    print("price:" + str(p.getprice()))
    
    c.registerCustomer()
    c.login()
    cart.addItem()
    o.confirmOrder()
    pay.makePayment()
    s.trackingShipment()

if __name__ == "__main__":
    main()
