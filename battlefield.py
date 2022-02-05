from herd import Herd
from fleet import Fleet

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()  
        

    def display_welcome(self):
        print("WELCOME LADIES AND GENTLEMAN TO THE BATTLE OF THE CENTRY!!!!")

    def battle(self): 
        while (len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0):
            self.robo_turn()
            self.dino_turn()


    def dino_turn(self):
        print("Select a dino to attack with")
        self.dino_oppo()
        user_dino_choice = int(input())
        print("Select a robot to attack")
        self.robo_oppo()
        user_robot_choice = int(input())
        self.herd.dinosaurs[user_dino_choice].attack(self.fleet.robots[user_robot_choice])
        if self.fleet.robots[user_robot_choice].health <= 0:
            print(f'{self.fleet.robots[user_robot_choice].name} has been eliminated')
            self.fleet.robots.remove(self.fleet.robots[user_robot_choice])

    def robo_turn(self):
        print("Select a robot to attack with")
        self.robo_oppo()
        user_robot_choice = int(input())
        print("Select a Dinosaur to attack")
        self.dino_oppo()
        user_dino_choice = int(input())
        self.fleet.robots[user_robot_choice].attack(self.herd.dinosaurs[user_dino_choice])
        if self.herd.dinosaurs[user_dino_choice].health <= 0:
            print(f'{self.herd.dinosaurs[user_dino_choice].dino_name} has been eliminated')
            self.herd.dinosaurs.remove(self.herd.dinosaurs[user_dino_choice])

    def dino_oppo(self): 
        index = 0
        for dino in self.herd.dinosaurs:
            print(f'Press {index} to select {dino.dino_name}')
            index += 1
        
   
    def robo_oppo(self):
        index = 0
        for robot in self.fleet.robots:
            print(f'Press {index} to select {robot.name}')
            index += 1
        

    def display_winners(self): # logic will be if dino team list is at 0 then robots won, elif robot team list is at 0 then dino's won
        if len(self.fleet.robots) <= 0:
            print('AND THE WINNER IS ..........  THE DINOSAURS!!!')
        elif len(self.herd.dinosaurs) <= 0:
            print('AND THE WINNER IS ..........  THE ROBOTS!!!')
            