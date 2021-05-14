

from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.turn = 1
        self.user_selector = 0
        self.enemy_selector = 0
        self.fleet = Fleet()
        self.herd = Herd()
        self.user_choice = ""
        self.user = ()
        self.enemy = ()

    def run_game(self):
        self.display_welcome()
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.user_choice = input('Choose "dinos" or "robots"')
        while not self.user_choice == 'dinos' or self.user_choice == 'robots':
            self.user_choice = input('Incorrect Input: Choose "dinos" or "robots"')
        if self.user_choice == "dinos":
            self.user = self.herd.dinosaurs
            self.enemy = self.fleet.robots
            print("\nYou're team of dinos consists of:")
            for dino in self.user:
                print(f'Type - {dino.type}, Energy - {dino.energy}, Power - {dino.attack_power},Health - {dino.health}')
            print("\nYou're enemy robots are:")
            for robo in self.enemy:
                print(f'Name - {robo.name}, Energy - {robo.power_level}, Health - {robo.health}, Weapon - {robo.weapon.type} (atk) {robo.weapon.attack_power}')
        else:
            self.user = self.fleet.robots
            self.enemy = self.herd.dinosaurs
            print("\nYou're team of robots consists of:")
            for robo in self.user:
                print(f'Name - {robo.name}, Energy - {robo.power_level}, Health - {robo.health}, Weapon - {robo.weapon.type} (atk) {robo.weapon.attack_power}')
            print("\nYou're enemy dinosaurs are:")
            for dino in self.enemy:
                print(f'Type - {dino.type}, Energy - {dino.energy}, Power - {dino.attack_power},Health - {dino.health}')

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self, user, enemy):
        print("Battle")






