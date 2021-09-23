# Algo :
# 1. develop the interface
# 2. predefined list
# 3. instruction
# 4. 
import random
def hangman():
    with open("hangmanWords.txt") as f :
        allWords = f.read()
        words = list(map(str,allWords.split()))
        word = random.choice(words)
    validLetters ='abcdefghijklmnopqrstuvwxyz'
    turns = 10
    user_guess =''
    
    while len(word)>0:
        main =""
        missed = 0

        for letter in word:
            if letter in user_guess:
                main = main + letter
            else:
                main = main +"_" +""
        
        if main == word:
            print(main)
            print("You Won!!!")
            break

        print("Guess The Word ",main)
        guess = input()


        # checking character valid?
        if guess in validLetters:
            user_guess = user_guess + guess
        else:
            print("Enter a valid character") 
            guess = input()

        #when turns-- ,print the figure   
        if guess  not in word:
            turns = turns -1 
            print( "\n" , turns , " turns left ")
            if(turns == 9):
                print("=========")
            if(turns == 8):
                print("=========")
                print("    O    ")
            if(turns == 7):
                print("=========")
                print("    O    ")
                print("    |    ")
            if(turns == 6):
                print("=========")
                print("    O    ")
                print("    |    ")
                print("    /    ")
            if(turns == 5):
                print("=========")
                print("    O    ")
                print("    |    ")
                print("   / \   ")
            if(turns == 4):
                print("=========")
                print("  \ O    ")
                print("    |    ")
                print("   / \   ")
            if(turns == 3):
                print("=========")
                print("  \ O /  ")
                print("    |    ")
                print("   / \   ")
            if(turns == 2):
                print("=========")
                print("  \ O /| ")
                print("    |    ")
                print("   / \   ")
            if(turns == 1):
                print("=========")
                print("  \ O_|/ ")
                print("    |    ")
                print("   / \   ")
            if(turns == 0):
                print("YOU Lose!!!")
                print("You A Let Kind MAn Die!!!")
                print("    O_|  ")
                print("   /|\   ")
                print("   / \   ")
                print("Word is : " ,word)
                break

name = input("Enter your name : ")
print("Welcome" , name)
print("^^^^^^^^^^^^")
print("Try to guess the word in less than 10 attempts ")
hangman()
print()


