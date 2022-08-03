import numpy as np
import time

def main():

    options = {'rock' : 'scissors', 'scissors' : 'paper', 'paper' : 'rock'}

    player = input("write rock, scissors or paper: ")
    
    while player not in {'rock', 'scissors', 'paper'}:
        print("You tiped an error... .-.")
        player = input("Write Rock, Scissors or paper: ")
        
    cpu = np.random.choice(['rock', 'scissors', 'paper'])

    time.sleep(.5)
    print("\nYou chose: ", player)
    print("The cpu chose: ", cpu, '\n')
    time.sleep(2)

    if options[player] == cpu :
        print(" You win!")
        
    elif options[cpu] == player :
        print(" You lose!")
        
    else :
        print("Draw")


if __name__ == '__main__' :
    main()