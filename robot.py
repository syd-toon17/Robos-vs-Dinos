from weapon import Weapon
class Robot:

    def __init__(self, name, health, weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Lazer Pistol', 20)
    
    def attack(self, dinosoar):
        pass