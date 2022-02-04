# add logic to robot attack() then test it, then do dino and test it
# test robo_oppo and see how it works and make one for dino_opp 

from herd import Herd
from fleet import Fleet

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.robots[0].attack(self.herd.dinosoars[0])
        pass
    
    def display_welcome(self):
        pass

    def battle(self): # while loop, while robot and dino list are greater than 0 it will loop through dino_turn and robot_turen
        pass

    def dino_turn(self): # add attack method and make sure you can test 1 round of fighting
        pass

    def robo_turn(self):
        pass

    def dino_oppo(self): # use a for loop to print out all of the opetions for the user to pick from
        pass
   
    def robo_oppo(self):
        # index = 0
        # for robot in self.fleet.robots:
        #     print(f'Press {index} to select {robot.name}')
        #     index += 1
        pass

    def display_winners(self):
        pass