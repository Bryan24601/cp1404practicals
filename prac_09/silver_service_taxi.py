from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super.__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.current_fare_distance = 0
        self.flagfall = 4.50

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall}"
