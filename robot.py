import random

from weapon import Weapon



class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon(input("Name this robot's weapon:"), random.randint(10, 30))

    def attack_dinosaur(self, dino):
        dino.health -= self.weapon.attack_power
        self.power_level -= 10

