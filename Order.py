# Name: Samidha Mote 
# Roll no.: 2643
#
# Order class represents an order placed by the customer.
# It stores order details such as order id, total amount, order date and order status.
# It qalso provides methods to confirm or cancel an order.
class Order:
    def __init__(self):
        self.orderId = None
        self.totalAmount = None
        self.orderDate = None
        self.status = None

    # Sets the order id
    def setOrderId(self, orderId):
        self.orderId = orderId
    # Return the order id
    def getOrderId(self):
        return self.orderId

    # Sets the order date
    def setOrderDate(self, orderDate):
        self.orderDate = orderDate
    # Returns the order date
    def getOrderDate(self):
        return self.orderDate

    # Sets the total amount of the order
    def setTotalAmount(self, totalAmount):
        self.totalAmount = totalAmount
    # Returns the total amount of the order
    def getTotalAmount(self):
        return self.totalAmount

    # Sets status of the order
    def setStatus(self, status):
        self.status = status
    # Returns the current status of the order
    def getStatus(self):
        return self.status

    # Confirms the customer order
    def confirmOrder(self):
        print("order has been confirmed")

    # Cancels the order
    def cancelOrder(self):
        print("order has been cancelled")
