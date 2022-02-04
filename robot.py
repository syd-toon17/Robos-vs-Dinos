from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon = Weapon('Lazer Pistol', 15)
    # when we call this method on battlefield we will pass in a dino object that we want our robot to fight

    def attack(self, dinosoar):
        dinosoar.health -= self.weapon.attack_power
        print(f"{dinosaur.dino_name} took an attack, {dinosaur.dino_name}'s new health is {dinosaur.health}.")
        


    