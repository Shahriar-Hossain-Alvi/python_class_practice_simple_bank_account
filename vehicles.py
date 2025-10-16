class Vehicle:
    def __init__(self, brand, model):
        self.brand_name = brand
        self.vehicle_model = model

    def info(self):
        print(f"Brand: {self.brand_name} | Model: {self.vehicle_model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
    
    def info(self):
        print(f"Brand: {self.brand_name} | Model: {self.vehicle_model} | Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc
    
    def info(self):
        print(f"Brand: {self.brand_name} | Model: {self.vehicle_model} | Engine: {self.cc}cc")

car1 = Car("Toyota", "Corolla", 5)
car1.info()

bike1 = Bike("Yamaha", "R15", 155)
bike1.info()