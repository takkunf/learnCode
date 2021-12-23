import random


def main() :
    vida = 4
    aleatorio = random.randint(1, 100)
    elegido = int(input("Elige un numero del 1 al 100, tienes 5 vidas :  "))
    
    while aleatorio != elegido and vida != 0 :
        

        if aleatorio > elegido :
            print("Elige un numero mayor, te quedan "  + str(vida) + " vidas", end = " ")

        else:
            print("Elige un numero menor, te quedan "  + str(vida) + " vidas", end = " ")
        
        vida -= 1
        elegido = int(input(" :  "))
        

    if vida != 0 :
        print("Al fin lograste algo en la vida, Maldito inutil! :D ")
    
    else :
        print("No logras nada en la vida... porque sigues respirando???? ")



if __name__ == '__main__' :
    main()