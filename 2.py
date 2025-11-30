# Exercise 2

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, amount):
        self.current_speed += amount

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Speed after accelerating:", car.current_speed)

car.accelerate(-200)
print("Speed after braking:", car.current_speed)
print()
