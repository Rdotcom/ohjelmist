import random


class Race:
    def __init__(self, racename, distance, cars):
        self.racename = racename
        self.distance = distance
        self.cars = cars

    def tunti_kuluu(self):
        for car in self.cars:
            speeding = random.randint(1, 15) #nopeus ei enää negatiivinen, jottei kilpailijat aja väärään suuntaan
            car.drive(speeding)

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.racename}")
        print(f"{'Auto':<10}{'Matka (km)':<15}{'Nopeus (km/h)':<15}{'Aika (h)':<15}")
        for car in self.cars:
            print(f"{car.car:<10}{car.distance:<15.2f}{car.speed:<15.2f}{car.time:<15.2f}")

    def kilpailu_ohi(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


class Auto:
    def __init__(self, car, speed, distance, time):
        self.car = car
        self.speed = speed
        self.distance = 0
        self.time = 0

    def drive(self, time):
        self.distance += self.speed * time
        self.time += time

''' #tehtävä 4
if __name__ == "__main__":
    auto1 = Auto("Toyota", 100,0,0)
    auto2 = Auto("XPeng", 85,0,0)
    kilpailu = Race("Kilpailu F", 100, [auto1, auto2])
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()

    kilpailu.tulosta_tilanne()
'''


def main():
    carlist = []
    for i in range(10):
        racer = Auto(f"Auto{i+1}", random.randint(80,120),0,0)
        carlist.append(racer)

    suuri_romuralli = Race("Suuri Romuralli", 8000, carlist)

    tuntivali = 10
    tunti = 0

    while not suuri_romuralli.kilpailu_ohi():
        for i in range(10):
            suuri_romuralli.tunti_kuluu()
            tunti += 1
            # ei toimi
            if tunti % tuntivali == 0:
                print(f"Kilpailu on kestänyt {tunti} tuntia")
                suuri_romuralli.tulosta_tilanne()

    print("Kilpailu on päättynyt!")
    suuri_romuralli.tulosta_tilanne()

if __name__ == "__main__":
    main()