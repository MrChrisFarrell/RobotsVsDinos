import random

from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet = self.fleet.create_fleet()
        self.herd = self.herd.create_herd()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self):
        roll = random.randint(1, 7)
        if roll % 2 == 0:


x = Herd()

x.create_herd()
for dino in x.dinosaurs:
    print(dino.type, dino.energy, dino.attack_power, dino.health)

y = Fleet()

y.create_fleet()
for robot in y.robots:
    print(robot.name, robot.health, robot.power_level, robot.weapon.type, robot.weapon.attack_power)
