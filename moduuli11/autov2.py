class Car:
    def __init__(self, plate, maxspeed):
        self.plate = plate
        self.maxspeed = maxspeed
        self.distance = 0
        self.speed = maxspeed


    def Drive(self, time):
        self.distance += self.maxspeed * time

class ElectricCar(Car):
    def __init__(self, plate, maxspeed, battery):
        super().__init__(plate, maxspeed)
        self.speed = 0
        self.battery = battery

    def info(self):
        print(f"Plate: {self.plate}\nMax speed: {self.maxspeed} km/h\nBattery: {self.battery} kWh")


class GasCar(Car):
    def __init__(self, plate, maxspeed, fueltank):
        super().__init__(plate, maxspeed)
        self.tankfuel = fueltank

    def info(self):
        print(f"Plate: {self.plate}\nMax speed: {self.maxspeed} km/h\nFuel tank: {self.tankfuel} l")


if __name__ == "__main__":
    sähkö = ElectricCar("ABC-15", 180,52.5)
    sähkö.info()
    bensa = GasCar("ABC-123", 165, 32.3)
    bensa.info()
    print()
    sähkö.Drive(3)
    bensa.Drive(3)
    print(f"Electric car distance: {sähkö.distance:.0f} km")
    print(f"Gas car distance: {bensa.distance:.0f} km")