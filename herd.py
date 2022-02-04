from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
        

    def create_herd(self):
        dino_one = Dinosaur('Tiny')
        self.dinosaurs.append(dino_one)

        dino_two = Dinosaur('Rex')
        self.dinosaurs.append(dino_two)
        
        dino_three = Dinosaur('Arlo')
        self.dinosaurs.append(dino_three)
        