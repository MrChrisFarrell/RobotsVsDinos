import random

from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        while len(self.dinosaurs) < 3:
            self.dinosaurs.append(Dinosaur(input("Name a type of dinosaur"), random.randint(1, 6)))






