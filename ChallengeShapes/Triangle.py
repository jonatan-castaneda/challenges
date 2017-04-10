
class Triangle:

    def __init__(self):
        self.name = "Triangulo"
        self.base = 0
        self.height = 0

    def setBase(self, base):
        self.base = base

    def setHeight(self, height):
        self.height = height
    
    def getArea(self):
        return (self.height * self.base) / 2

    def getPerimeter(self):
        return self.base * 3
    
    def getName(self):
        return self.name