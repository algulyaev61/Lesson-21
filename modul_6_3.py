import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.x = dx * self.speed
            self.y = dy * self.speed
            self.z = dz * self.speed

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, I'm peaceful:")
        else:
            print(f"Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.z = abs(self.z - dz * (self.speed / 2))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()
