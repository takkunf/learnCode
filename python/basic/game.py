import random


def main() :
    life = 4
    rand = random.randint(1, 100)
    chosenone = int(input("Choose a number from 1 to 100, you have 5 lives :  "))
    
    while rand != chosenone and life != 0 :
        

        if rand > chosenone :
            print("Choose a higher number, you have "  + str(life) + " lives", end = " ")

        else:
            print("Choose a lower number, you have"  + str(life) + " lives", end = " ")
        
        life -= 1
        chosenone = int(input(" :  "))
        

    if life != 0 :
        print("You win!!")
    
    else :
        print("You lose... :c The number was " + str(rand))



if __name__ == '__main__' :
    main()