from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        robot_one = Robot('Baymax')
        self.robots.append(robot_one)

        robot_two = Robot('WALL-E')
        self.robots.append(robot_two)

        robot_three = Robot('Carl the Robot')
        self.robots.append(robot_three)
        