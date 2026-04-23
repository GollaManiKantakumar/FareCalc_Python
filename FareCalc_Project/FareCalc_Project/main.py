from fare_logic import compute_price
from utils import print_bill


def start():
    try:
        km = float(input("Distance (km): "))
        vtype = input("Vehicle (Economy/Premium/SUV): ").strip()
        hr = int(input("Hour (0-23): "))

        if hr < 0 or hr > 23:
            print("Invalid time entered")
            return

        amount, peak = compute_price(km, vtype, hr)

        print_bill(km, vtype, hr, amount, peak)

    except ValueError as msg:
        print(msg)
    except:
        print("Invalid input, please try again.")


if __name__ == "__main__":
    start()