class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
