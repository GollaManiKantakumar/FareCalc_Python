def print_bill(km, vtype, hr, amount, peak):
    print("\n" + "-" * 30)
    print("CityCab Ride Summary")
    print("-" * 30)

    print("Distance :", km, "km")
    print("Vehicle  :", vtype.title())   # Looks clean
    print("Time     :", str(hr) + ":00")

    if peak:
        print("Surge    : Yes (Peak hours)")
    else:
        print("Surge    : No")

    print("-" * 30)
    print("Final Fare : ₹", amount)
    print("-" * 30)