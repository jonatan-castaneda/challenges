from Triangle import Triangle
from Circle import Circle
from Square import Square

if __name__ == '__main__':
    base = 10
    height = 20
    ratio = 15
    name = input("Introduce el nombre de la figura: ")
    if name == "triangulo":
        figure = Triangle()
        figure.setBase(base)
        figure.setHeight(height)
        print("El área del %s es: %s y el perímetro es: %s" % (figure.getName(), figure.getArea(), figure.getPerimeter()) )
    elif name == "circulo":
        figure = Circle()
        figure.setRatio(ratio)
        print("El área del %s es: %s y el perimetro es: %s" % (figure.getName(), figure.getArea(), figure.getPerimeter()) )
    elif name == "cuadrado":
        figure = Square()
        figure.setBase(base)
        print("El área del %s es: %s y el perimetro es: %s" % (figure.getName(), figure.getArea(), figure.getPerimeter()) )