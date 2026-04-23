from services.auth_service import AuthService
from services.fare_service import FareService
from services.ride_service import RideService
from utils.bills import print_bill

auth = AuthService()
fare_service = FareService()
ride_service = RideService()


def user_menu(user):
    while True:
        print("\n1. Book Ride")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":


            while True:
                try:
                    km = float(input("Distance: "))
                    hour = int(input("Hour (0-23): "))

                    if hour < 0 or hour > 23:
                        print("Invalid hour. Please enter between 0-23.")
                        continue

                    vehicle = input("Vehicle (Economy/Premium/SUV): ")

                    # Try booking ride
                    ride = ride_service.book_ride(user, km, vehicle, hour, fare_service)

                    # If success → exit loop
                    break

                except ValueError as e:
                    print(e)
                    print("Valid vehicles: Economy, Premium, SUV")
                except:
                    print("Invalid input. Please try again.")

            # ✅ After successful booking
            print_bill(ride)

            pay = input("Pay now? (yes/no): ")
            if pay.lower() == "yes":
                ride_service.pay_bill(ride)

        elif choice == "2":
            if not user.transactions:
                print("No transactions found")
            else:
                for ride in user.transactions:
                    print_bill(ride)

        elif choice == "3":
            break

        else:
            print("Invalid choice")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc = input("Account No: ")
            name = input("Name: ")
            pwd = input("Password: ")
            auth.register(acc, name, pwd)

        elif choice == "2":
            acc = input("Account No: ")
            user = auth.login(acc)

            if user:
                user_menu(user)

        elif choice == "3":
            print("Thank you for using CityCab 🚖")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()