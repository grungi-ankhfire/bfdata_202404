class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride(self, duration):
        self.distance += self.speed * duration

class Bike(Vehicle):
    def __init__(self):
        super().__init__(15)

class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05
    
    def ride(self, duration):
        travel = duration * self.speed
        travel_max = self.fuel / self.consumption
        travel = min(travel, travel_max)
        self.distance += travel
        self.fuel -= travel * self.consumption


bike = Bike()
bike.ride(1)
print(bike.distance)
car = Car()
car.ride(10)
print(car.distance)
print(car.fuel)

