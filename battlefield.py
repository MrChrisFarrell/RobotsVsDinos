import random

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
        self.user = None
        self.enemy = ()
        self.user_attacker = ()
        self.enemy_attacked = ()
        self.enemy_attacker = ()
        self.user_attacked = ()


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
        self.battle(self.user)

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self):
        if self.turn % 2 == 1:
            if self.user == self.herd.dinosaurs:
                self.dino_turn()
                if self.enemy_attacked.health < 1:
                    print(f"{self.enemy_attacked.name} has died!")
                    del self.enemy[self.enemy_selector]
            else:
                self.robot_turn()
                if self.user_attacked.health < 1:
                    print(f"{self.user_attacked.name} has died!")
                    del self.user[self.user_selector]
        else:
        self.enemy_selector = 0

    def dino_turn(self):
        if self.user == self.herd.dinosaurs:
            self.user_attacker = self.user[self.user_selector]
            print(f"\nYou're attacker is: Type - {self.user_attacker.type}, Energy - {self.user_attacker.energy}, Power - {self.user_attacker.attack_power},Health - {self.user_attacker.health}")
            print(f'\nPick an enemy to attack!\n')
            self.show_robo_opponent_options()
            self.enemy_selector = int(input("Enter enemy number:"))
            self.enemy_attacked = self.enemy[self.enemy_selector]
            print(f"\n{self.user_attacker.type} attacks {self.enemy_attacked.name} for {self.user_attacker.attack_power} damage!")
            self.user_attacker.attack_robot(self.enemy_attacked)
            self.user_selector += 1
        else:
            self.user_selector = random.randint(0, len(self.user))
            self.enemy_attacker = self.enemy[random.randint(0, len(self.enemy))]
            self.user_attacked = self.user[self.user_selector]
            print(f"\n{self.enemy_attacker.type} attacks {self.user_attacked.name} for {self.enemy_attacker.attack_power} damage!")
            self.enemy_attacker.attack_robot(self.user_attacked)

    def show_robo_opponent_options(self):
        for robo in self.enemy:
            print(f'Enter "{self.enemy_selector}" - {robo.name}, Energy - {robo.power_level}, Health - {robo.health}, Weapon - {robo.weapon.type} (atk) {robo.weapon.attack_power}')
            self.enemy_selector += 1

    def robot_turn(self):
        if self.user == self.fleet.robots:
            self.user_attacker = self.user[self.user_selector]
            print(f"\nYou're attacker is: Name - {self.user_attacker.name}, Energy - {self.user_attacker.power_level}, Health - {self.user_attacker.health}, Weapon - {self.user_attacker.weapon.type} (atk) {self.user_attacker.attack_power}")
            print("\nPick an enemy to attack!\n")
            self.show_dino_opponent_options()
            self.enemy_selector = int(input("Enter enemy number:"))
            self.enemy_attacked = self.enemy[self.enemy_selector]
            print(f"\n{self.user_attacker.name} attacks {self.enemy_attacked.type} for {self.user_attacker.weapon.attack_power} damage!")
            self.user_attacker.attack_dinosaur(self.enemy_attacked)
            self.user_selector += 1
        else:
            self.user_selector = random.randint(0, len(self.user))
            self.enemy_attacker = self.enemy[random.randint(0, len(self.enemy))]
            self.user_attacked = self.user[self.user_selector]
            print(f"\n{self.enemy_attacker.name} attacks {self.user_attacked.type} for {self.enemy_attacker.weapon.attack_power} damage!")
            self.enemy_attacker.attack_dinosaur(self.user_attacked)

    def show_dino_opponent_options(self):
        for dino in self.enemy:
            print(f'Enter "{self.enemy_selector}" - {dino.type}, Energy - {dino.energy}, Health - {dino.health}, Power - {dino.attack_power}')
            self.enemy_selector += 1
