class VehicleLocationError(Exception):
    pass

class Vehicle:
    def __init__(self, make, model, year_of_manufacture, number_of_wheels = 4):
        self.make = make
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.passengers = []
        self.current_location = (None,)
        self.number_of_wheels = number_of_wheels

    def move(self, move_from, move_to):
        if self.current_location == move_from:
            self.current_location = move_to
        else:
            raise VehicleLocationError


"""please implement the rest of the Bike functionality"""
class Bike(Vehicle):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)
        self.number_of_wheels = 2

    def move(self, move_from, move_to):
        if self.current_location == move_from:
            self.current_location = move_to
        else:
            raise VehicleLocationError

class Car(Vehicle):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)


class Truck(Vehicle):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)
        self.passengers = None

    def move(self):
        return "I move slowly"


class Bus(Vehicle):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)


b = Bus("Leyland", "BE10", 2022)
print(b.make)
print(b.model)
print(b.year_of_manufacture)
print(b.passengers)
print(b.current_location)
try:
    location = b.move((None,), (2, 3))
except VehicleLocationError:
    print("cant do that")
print(b.current_location)

t = Truck("Ford", "BE11", 2020)
location = t.move()
print(location)

bike = Bike("Yamaha", "YZ", 2022)
print(bike.make)
print(bike.model)
print(bike.year_of_manufacture)

try:
    location = bike.move((None,), (1, 2))
    print(f"Bike moved to: {bike.current_location}")
except VehicleLocationError:
    print("can't do that")