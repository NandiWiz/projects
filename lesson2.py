class AlreadyRunning(Exception):
    pass
class AlreadyStopped(Exception):
    pass
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.brand} {self.model} is now running.")
            return
        raise AlreadyRunning
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.brand} {self.model} has stopped.")
            return
        raise AlreadyStopped
    def __str__(self):
        return f"{self.brand} {self.model}"


if __name__ == "__main__":
    my_car = Car("Honda", "Civic", 2017)
    print(my_car)
    while True:
        try:
            my_car.start()
            my_car.start()
        except AlreadyRunning:
            print("Can't start a car which is already started")
        except AlreadyStopped:
            print("Can't stop a car which is already stopped")
        finally:
            break