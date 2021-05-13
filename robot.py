from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 0
        self. health = 0
        self.weapon = Weapon()
