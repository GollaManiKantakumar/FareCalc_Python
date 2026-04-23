class Ride:
    def __init__(self, km, vehicle, hour, amount, paid=False):
        self.km = km
        self.vehicle = vehicle
        self.hour = hour
        self.amount = amount
        self.paid = paid