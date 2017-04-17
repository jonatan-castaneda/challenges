import random

class Horse:
    def __init__(self):
        self.avance = 0

    def avanza(self):
        self.avance += random.randrange(0,6)

    def getAvance(self):
        return self.avance