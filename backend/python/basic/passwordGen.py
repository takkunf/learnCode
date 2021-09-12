import random


def passwordGenerator():
    upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    number = ['1','2','3','4','5','6','7','8','9','0']
    symbol = ['!','@','#','$','%','^','&','*','_','-','+',' ']
    
    characters = upperCase + lowerCase + number + symbol

    password = []

    for i in range(15):
        randomCharacters = random.choice(characters)
        password.append(randomCharacters)

    password = "".join(password)
    return password


def main():
    password = passwordGenerator()
    print("your new password is: " + password)


if __name__ == '__main__' :
    main()