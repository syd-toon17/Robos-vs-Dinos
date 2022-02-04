class Dinosoar:
    
    def __init__(self, name):
        self.dino_name = name
        self.attack_power = 15
        self.health = 50

    def attack(self, robot):
        robot.health -= self.attack_power
        pass