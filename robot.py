import random

from weapon import Weapon



class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 10
        self. health = 10
        self.weapon = Weapon(input("Name this robot's weapon:"), random.randint(1, 6))

    def attack_dinosaur(self, dino):
        dino.health -= self.weapon.attack_power
        self.power_level -= 2

