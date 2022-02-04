from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        self.robots.append(robot_one = Robot('Baymax'))
        self.robots.append(robot_two = Robot('WALL-E'))
        self.robots.append(robot_three = Robot('Carl the Robot'))
        pass