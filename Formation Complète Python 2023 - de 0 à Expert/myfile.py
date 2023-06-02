import random
import os

number_1 = random.randint(0,5)
number_2 = random.randint(0,5)
if number_1 == number_2:
    print(f"{number_1} et {number_2}are equal")
elif number_1 > number_2:
    print(f"{number_1} are bigger than {number_2}")
elif number_1 < number_2:
    print(f"{number_1} are smaller than {number_2}")

r = random.randrange(0,100,5)
print(r)
