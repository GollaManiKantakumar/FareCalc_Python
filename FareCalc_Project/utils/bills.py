def print_bill(ride):
    print("\n----- BILL -----")
    print("Distance:", ride.km, "km")
    print("Vehicle:", ride.vehicle)
    print("Time:", ride.hour)
    print("Amount:", ride.amount)
    print("Status:", "Paid" if ride.paid else "Unpaid")
    print("----------------\n")