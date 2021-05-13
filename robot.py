from weapon import Weapon

class Robot:
    def __init__(self, name, power, health, weapon):
        self.name = name
        self.power_level = int(power)
        self. health = int(health)
        self.weapon = Weapon(weapon)
        