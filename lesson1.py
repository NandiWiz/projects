class Plane:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_flying = False

    def take_off(self):
        if not self.is_flying:
            self.is_flying = True
            self.speed = 150
            print(
                f"The {self.year} {self.color} {self.brand} {self.model} has taken off.")
        else:
            print("The plane is already in the air.")

    def land(self):
        if self.is_flying:
            self.is_flying = False
            self.speed = 0
            self.altitude = 0
            print(
                f"The {self.year} {self.color} {self.brand} {self.model} has landed.")
        else:
            print("The plane is already on the ground.")

        def __str__(self):
            return self.brand + self.model

if __name__ == "__main__":
    my_plane = Plane("Boeing", "757", 2022, "white")
    print(my_plane)
    my_plane.take_off()
    my_plane.land()