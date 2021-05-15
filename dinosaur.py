from robot import Robot


class Dinosaur:
    def __init__(self, breed, attack_power):
        self.type = breed
        self.energy = 100
        self.attack_power = int(attack_power)
        self.health = 100

    def attack_robot(self, robot):
        if self.energy < 10:
            print(f"{self.type} is out of energy and can't attack... Quick nap for 50%")
            self.energy += 50
        else:
            robot.health -= self.attack_power
            self.energy -= 10

