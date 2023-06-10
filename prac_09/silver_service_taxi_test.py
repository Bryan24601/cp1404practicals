from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    first_taxi = SilverServiceTaxi("Super Taxi 1", 200, 2)
    first_taxi.start_fare()
    first_taxi.drive(18)
    print(first_taxi)
    print(first_taxi.get_fare())


main()
