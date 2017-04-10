
class Circle:

    def __init__(self):
        self.name = "Circle"
        self.ratio = 0
    
    def setRatio(self, ratio):
        self.ratio = ratio

    def getArea(self):
        return (3.1416)*(self.ratio*self.ratio)
    
    def getPerimeter(self):
        return 2*(3.1416)*self.ratio

    def getName(self):
        return self.name