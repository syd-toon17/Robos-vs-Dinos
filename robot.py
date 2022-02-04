from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Lazer Pistol', 15)
    # when we call this method on battlefield we will pass in a dino object that we want our robot to fight
    def attack(self, dinosoar): # diosaur.health -= self.weapon.attack_power use print to inform the user 
        pass