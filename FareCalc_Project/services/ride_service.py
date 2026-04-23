from models.ride import Ride

class RideService:

    def book_ride(self, user, km, vehicle, hour, fare_service):
        amount = fare_service.calculate(km, vehicle, hour)

        ride = Ride(km, vehicle, hour, amount)
        user.transactions.append(ride)

        print("Ride booked successfully")
        return ride

    def pay_bill(self, ride):
        if ride.paid:
            print("Already paid")
        else:
            ride.paid = True
            print("Payment successful")