import random
import string
from words import words
from livesVisual import lives_visual_dict

def getValidWord(words):
    word = random.choice(words) #randomly chooses something from words
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() #what the user has guessed
    lives = 8
    
    #getting user input
    while len(wordLetters) > 0 and lives > 0:
        #display letters used
        if lives != 1:
            print('You have', lives, 'lives and have used these letters: ', ' '.join(usedLetters))
        elif lives == 1:    
            print('You have', lives, 'live and have used these letters: ', ' '.join(usedLetters))
        
        #what current word is
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(wordList))
        
        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print()
                
            else: 
                lives = lives - 1
                print('\nYour letter,', userLetter, 'is not in the word.')
                
                
        elif userLetter in usedLetters:
            print('You have already guessed that letter. Please try again.')
            print() 
            
        else: 
            print('Invalid Letter. Please try again.')
            print() 
    
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You lose. The word was', word)
        print()
    else:
        print('You guessed the word,', word, "!!")
        print()
    
print()  
hangman()