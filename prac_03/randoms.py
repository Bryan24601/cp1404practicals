"""
Line 1:
smallest number: 5
largest number: 19

Line 2:
smallest number: 3
unable to produce a 4

Line 3:
smallest number: 2.5
biggest number: 5.499999999999999
"""

import random
lower_limit = 1
upper_limit = 100
random_number = random.randint(lower_limit, upper_limit + 1)
print(random_number)