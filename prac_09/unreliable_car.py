from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init(self, name, fuel, reliability):
        super().__init__(name, fuel, reliability)
        self.distance = 0

    def __str__(self):
        return f"{super().__str__()}, Distance travelled: {self.distance}km"

    def drive(self, distance):
        drive_chance = random.randint(1, 101)
        if drive_chance < self.reliability:
            distance_driven = super().drive(distance)
            self.distance += distance_driven
            return distance_driven
        else:
            return self.distance
