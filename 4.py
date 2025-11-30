import random

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

cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg, max_speed))

race_finished = False

while not race_finished:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

print("Race results:")
for car in cars:
    print(car.registration_number, "| Max:", car.max_speed,
          "| Speed:", car.current_speed,
          "| Distance:", int(car.travelled_distance))
