class Car:
    speed=0
    color=""
    name=""
    is_police=False
    directionlist={"left":"лево","right":"право"}

    def go(self):
        self.speed=60
        print (f"Машина {self.name} поехала")

    def stop(self):
        self.speed=0
        print (f"Машина {self.name} остановилась")

    def turn(self,direction=""):
        if direction :
            print (f"Машина {self.name} повернула на {self.directionlist[direction]}")

    def show_speed(self):
        print (f"Скорость машины {self.name} {self.speed} км/ч")

class TownCar(Car):

    def __init__(self):
        self.color="grey"
        self.name="TownCar"

    def show_speed(self):
        print (f"Скорость машины {self.name} {self.speed} км/ч")
        if int(self.speed)>60:
            print (f"Машины {self.name} превысила допустимую скорость!")

class WorkCar(Car):

    def __init__(self):
        self.color="white"
        self.name="WorkCar"

    def show_speed(self):
        print (f"Скорость машины {self.name} {self.speed} км/ч")
        if int(self.speed)>40:
            print (f"Машины {self.name} превысила допустимую скорость!")


class SportCar(Car):

    def __init__(self):
        self.speed=100
        self.color="red"
        self.name="SportCar"

    def show_speed(self):
        print (f"Скорость машины {self.name} {self.speed} км/ч")

class PoliceCar(Car):

    def __init__(self):
        self.speed=90
        self.color="blue"
        self.name="PoliceCar"




c=Car()
c.name="Тачка"
c.go()
c.turn("left")
c.show_speed()
c.stop()

t=TownCar()
t.go()
t.turn("right")
t.speed=80
t.show_speed()
t.stop()

s=SportCar()
s.go()
s.speed=180
s.show_speed()
s.stop()

p=PoliceCar()
p.go()
p.show_speed()
p.stop()

w=WorkCar()
w.go()
w.turn("right")
w.show_speed()
w.stop()


