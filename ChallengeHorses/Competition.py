from Horse import Horse

if __name__ == '__main__':
    horse1 = Horse()
    horse2 = Horse()
    while(True):
        horse1.avanza()
        horse2.avanza()
        print("Avance del Caballo 1: %s" % horse1.getAvance())
        print("Avance del caballo 2: %s" % horse2.getAvance())
        print("")
        if horse1.getAvance() >= 20 and horse2.getAvance() >= 20:
            print("Empate!!")
            break
        elif horse1.getAvance() >= 20 and horse2.getAvance() < 20:
            print("El caballo 1 ha ganado!")
            break
        elif horse2.getAvance() >= 20 and horse1.getAvance() < 20:
            print("El caballo 2 ha ganado!")
            break
