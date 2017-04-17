from Triangle import Triangle
from Circle import Circle
from Square import Square

class Figure():

    def __init__(self, name):
       self. name = name

    def getFigure(self, name):
        if name == "Triangle":
            return Triangle()
        elif name == "Circle":
            return Circle()
        elif name == "Square":
            return Square()

if __name__ == '__main__':
    base = 10
    height = 20
    ratio = 15
    name = input("Introduce el nombre de la figura: ")
    figure = Figure(name)
    figure = figure.getFigure(name)
    figure.setBase(base)
    if hasattr(figure, 'setHeight'):
        figure.setHeight(height)
    print("El área del %s es: %s y el perímetro es: %s" % (figure.getName(), figure.getArea(), figure.getPerimeter()) )
