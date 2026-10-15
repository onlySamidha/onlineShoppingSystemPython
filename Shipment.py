# Name: Samidha Mote 
# Roll no.: 2643
#
# Shipment class represents the shipment details of an order.
# It stores information such as shipment id, tracking number, shipment date and delivery status.
# It also provides a method to track the shipment.
class Shipment:
    def __init__(self):
        self.shipmentId = None
        self.trackingNumber = None
        self.shipmentDate = None
        self.deliveryStatus = None

    # Tracks the shipment of the customer order and displays the shipment tracking status.
    def trackingShipment(self):
        print("Tracking shipment")
