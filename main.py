from herd import Herd
from fleet import Fleet


x = Herd()

x.create_herd()
for dino in x.dinosaurs:
    print(dino.type, dino.energy, dino.attack_power, dino.health)

y = Fleet()

y.create_fleet()
for robot in y.robots:
    print(robot.name, robot.health, robot.power_level, robot.weapon.type, robot.weapon.attack_power)
