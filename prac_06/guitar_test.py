from prac_06.guitar import Guitar

name_test1 = "Gibson L-5 CES"
year_test1 = 1922
cost_test1 = 16035.40

name_test2 = "Another Guitar"
year_test2 = 2000
cost_test2 = 200

guitar_1 = Guitar(name_test1, year_test1, cost_test1)
guitar_2 = Guitar(name_test2, year_test2, cost_test2)
print("{} get_age() - Expected 101. Got {}".format(guitar_1.name, guitar_1.get_age()))
print("{} get_age() - Expected 23. Got {}".format(guitar_2.name, guitar_2.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(guitar_1.name, guitar_1.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(guitar_2.name, guitar_2.is_vintage()))