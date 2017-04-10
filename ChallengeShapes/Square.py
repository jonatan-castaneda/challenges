class Square:
    
    def __init__(self):
        self.name = "Cuadrado"
        self.base = 0
    
    def setBase(self, base):
        self.base = base
    
    def getArea(self):
        return self.base * self.base
    
    def getPerimeter(self):
        return self.base * 4

    def getName(self):
        return self.name