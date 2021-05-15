from robot import Robot


class Dinosaur:
    def __init__(self, breed, attack_power):
        self.type = breed
        self.energy = 100
        self.attack_power = int(attack_power)
        self.health = 100

    def attack_robot(self, robot):
        robot.health -= self.attack_power
        self.energy -= 10

