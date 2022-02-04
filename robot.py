from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Lazer Pistol', 15)
    # when we call this method on battlefield we will pass in a dino object that we want our robot to fight

    def attack(self, dinosoar):
        dinosoar.health -= self.weapon.attack_power
        print(f"{dinosoar} took an attack, {dinosoar}'s new health is {dinosoar.health}.")
    pass