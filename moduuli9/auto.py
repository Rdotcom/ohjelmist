import random
class Car: # tehtävä 1
    def __init__(self, plate, maxspeed, speed, distance):
        self.plate = plate
        self.maxspeed = maxspeed
        self.speed = 0
        self.distance = 0

    def info(self): # tehtävä 1
        print(f"Plate: {self.plate}\nMax speed: {self.maxspeed} km/h\nSpeed: {self.speed} km/h\nDistance: {self.distance} km")

    def accelerate(self, acceleration): # tehtävä 2
        new_speed = self.speed + acceleration
        if new_speed > self.maxspeed:
            self.speed = self.maxspeed
        elif new_speed < 0:
            self.speed = 0
            print("Braking...")
        else:
            self.speed = new_speed

    def drive(self, time): # tehtävä 3
        self.distance += self.speed * time
        print(f"Cars distance: {self.distance:.0f} km")

def create_racers(num_cars): # tehtävä 4
    cars = []
    for i in range(1,num_cars+1):
        maxspeed = random.randint(100,200)
        new_car = Car(f"ABC-{i}", maxspeed,0,0)
        cars.append(new_car)
    return cars

def race(): # tehtävä 4
    cars = create_racers(10)
    while True:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
        for car in cars:
            if car.distance >= 10000:
                print("Results:")
                for car in cars:
                    print(car.info())
                print(f"Car {car.plate} won!")
                return False

if __name__ == "__main__":
    race() # tehtävä 4
'''
    auto = Car("ABC-123", 142,60,2000)
    # tehtävä 1
    auto.info()

    # tehtävä 2
    print("Speeding")
    auto.accelerate(30)
    auto.accelerate(70)
    auto.accelerate(50)
    print("Car speed:", auto.speed)
    auto.accelerate(-200)
    print("Car speed:", auto.speed)
    
    # tehtävä 3
    auto.drive(1.5)
   '''

