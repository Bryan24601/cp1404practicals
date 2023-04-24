class Guitar:
    def __init__(self, name, year, cost):
        self.name = ""
        self.year = 0
        self.cost = 0

        self.name = name
        self.year = year
        self.cost = cost

    def guitar_information(self):
        guitar_information = "{} ({}): ${}".format(self.name, self.year, self.cost)
        return guitar_information

    def get_age(self):
        current_year = 2023
        return current_year - self.year
        # return "in {} the {} is:{} - {} = {}".format(current_year, self.name, current_year, self.year, self.age)

    def is_vintage(self):
        vintage_age = 50
        return self.get_age() >= vintage_age
