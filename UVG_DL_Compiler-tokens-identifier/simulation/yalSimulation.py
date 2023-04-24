
class yalSimulation():
    def __init__(self, file, AFD):
        self.AFD = AFD
        with open(file) as f:
            self.fileLines = f.readlines()
            
    def simulate(self):
        for line in self.fileLines:
            for character in line:
                print(character)
                
fl = yalSimulation('./yalex-tests/lectura.txt')
fl.simulate()