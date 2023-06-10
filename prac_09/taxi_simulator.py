from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill_to_date = 0.0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                if current_taxi.drive(distance):
                    trip_cost = current_taxi.get_fare()
                    bill_to_date += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                else:
                    print("Not enough fuel for this trip")

        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")


if __name__ == "__main__":
    main()
