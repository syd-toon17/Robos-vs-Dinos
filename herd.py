from dinosoar import Dinosoar

class Herd:

    def __init__(self):
        self.dinosoars = []
        self.create_herd()
        pass

    def create_herd(self):
        dino_one = Dinosoar('Tiny')
        self.dinosoars.append(dino_one)

        dino_two = Dinosoar('Rex')
        self.dinosoars.append(dino_two)
        
        dino_three = Dinosoar('Arlo')
        self.dinosoars.append(dino_three)
        pass