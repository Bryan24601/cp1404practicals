from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometersApp(App):
    miles = StringProperty("0")
    kilometers = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_text_change(self, text):
        self.miles = text
        self.calculate_kilometers()

    def handle_increment(self, value):
        try:
            miles = int(self.miles) + value
            self.miles = str(miles)
            self.calculate_kilometers()
        except ValueError:
            self.miles = "0"

    def calculate_kilometers(self):
        miles_to_kilometer = 1.60934
        try:
            miles = float(self.miles)
            kilometers = miles * miles_to_kilometer
            self.kilometers = "{}km".format(kilometers)
        except ValueError:
            self.kilometers = "0.0"


MilesToKilometersApp().run()


