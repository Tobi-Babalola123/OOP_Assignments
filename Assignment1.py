# Smartphone Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.__brand = brand  # Encapsulation: Private attribute
        self.model = model
        self.price = price

    def details(self):
        return f"Brand: {self.__brand}, Model: {self.model}, Price: ${self.price}"

    # Getter for brand
    def get_brand(self):
        return self.__brand

    # Setter for brand
    def set_brand(self, new_brand):
        self.__brand = new_brand


# Smartwatch Subclass
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, fitness_tracking):
        super().__init__(brand, model, price)
        self.fitness_tracking = fitness_tracking

    # Overriding details method (Polymorphism)
    def details(self):
        return f"{super().details()}, Fitness Tracking: {self.fitness_tracking}"


# Testing the classes
phone = Smartphone("Apple", "iPhone 15", 1200)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 300, "Yes")

print(phone.details())
print(watch.details())
