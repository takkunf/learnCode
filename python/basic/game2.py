import random
import os

def run():

    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        'python', 'java','javascript','php',
        'ruby','dart','swift','matlab','kotlin',
        'typescript', 'scala', 'pascal', 'scheme',
        'erlang', 'elixir', 'rust','postscript'
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 0

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(HANGMANPICS[attemps])
        
        letter = input('Elige una letra: ').lower()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
            
        if not found:
            attemps += 1
            
        if "_" not in spaces:
            os.system("clear")
            print('Ganaste!')
            break
            input()
        if attemps == 6:
            os.system("clear")
            print('Perdiste lol')
            break
            input()



if __name__ == '__main__':
    run()