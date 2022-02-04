class Dinosaur:
    
    def __init__(self, name):
        self.dino_name = name
        self.attack_power = 15
        self.health = 50

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{robot.name} took an attack, {robot.name}'s new health is {robot.health}.")
        