import os

if __name__ == '__main__':
    value = 3
    lista = [1,2,3,4,5,6,7]
    if value in lista:
        print("I find the element in the position " + str(lista.index(3)))
    else:
        print("Sorry, I couldn't find the element")  
