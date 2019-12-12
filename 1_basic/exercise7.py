# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it


class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2019 - self.year


# Test
car = Car(2000, 'A', 'B')
print(car.age())
