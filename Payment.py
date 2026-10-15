# Name: Samidha Mote 
# Roll no.: 2643
#
# Payment class storesthe payment details of a customer.
# It contains information such as payment id, payment method, payment amount and payment status.
# It also provides a method to process the payment.
class Payment:
    def __init__(self):
        self.paymentId = None
        self.paymentMethod = None
        self.amount = None
        self.paymentStstus = None

    # Processes the payment made by the customer.
    # Displays a successfull message.
    def makePayment(self):
        print("Payment Successful")
