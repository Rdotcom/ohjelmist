class Elevator: #tehtävä 1
    def __init__(self,lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.floor = lowest

    def floorup(self):
        if self.floor < self.highest:
            self.floor += 1
        else:
            print("Already on highest floor")

    def floordown(self):
        if self.floor > self.lowest:
            self.floor -= 1
        else:
            print("Already on lowest floor")

    def movefloor(self, targetfloor):
        if targetfloor < self.lowest:
            targetfloor = self.lowest
        elif targetfloor > self.highest:
            targetfloor = self.highest
        while self.floor < targetfloor:
            self.floorup()
        while self.floor > targetfloor:
            self.floordown()

class House: #tehtävä 2
    def __init__(self, lowest, highest, elevators):
        self.hissit = [Elevator(lowest, highest) for _ in range(elevators)]

    def moveelevator(self, elevatorsnumber ,targetfloor):
        if elevatorsnumber < 1 or elevatorsnumber > len(self.hissit):
            print("Error: Ei ole hissiä")
            return
        elevator = self.hissit[elevatorsnumber-1]
        elevator.movefloor(targetfloor)
        print(f"Hissi {elevatorsnumber} on kerroksessa {elevator.floor}")

    def firealarm(self):  #tehtävä 3
        for elevator in self.hissit:
            elevator.movefloor(elevator.lowest)
        print("Palohälytys! Kaikki hissit ovat alimmassa kerroksessa")



if __name__ == "__main__":
    #tehtävä 1
    hissi = Elevator(1,10)
    print("Hissin on alimmassa kerroksessa:",hissi.floor)
    targetfloor = 7
    hissi.movefloor(targetfloor)
    print("Hissi kerroksessa:",hissi.floor)
    hissi.movefloor(hissi.lowest)
    print("Hissi on alimmassa kerroksessa:",hissi.floor)

    # tehtävä 2
    talo = House(1,10,2)
    talo.moveelevator(1,5)
    talo.moveelevator(2,7)

    talo.firealarm()  # tehtävä 3