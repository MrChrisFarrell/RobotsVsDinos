from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []


    def create_fleet(self):
        if self.robots < 3:
            self.robots.append(Robot(input("Name a robot")))

