import random


def main() :
    life = 5
    r = random.randint(1, 100)
    num = int(input("Choose a number from 1 to 100, you have 5 lives :  "))
    
    while r != num and life != 0 :
        
        if r > num :
            print("Choose a higher number, you have "  + str(life) + " lives", end = " ")

        else:
            print("Choose a lower number, you have "  + str(life) + " lives", end = " ")
        
        num = int(input(" :  "))
        life -= 1
        

    if r == num :
        print("You win!!")
    
    else :
        print("You lose... :c The number was " + str(r))



if __name__ == '__main__' :
    main()