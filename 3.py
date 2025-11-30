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

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)

car.accelerate(100)   # set some speed
car.drive(1.5)        # drive 1.5 hours

print("Speed:", car.current_speed)
print("Distance:", car.travelled_distance)
print()
