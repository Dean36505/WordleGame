import random

def give_instructions():
    print('''\n Wordle is a word guessing game. You have five attempts
      to guess the hidden word. 
      (C) means the letter is in the word and in the correct postion
      (WP) means the letter is in the word but in the wrong position
      (NT) means the letter is not in the word''')

words = ["this", "five", "help", "lake", "pink", "cats"]


hidden_word = random.choice(words)



attempt = 5
def check_word(guess):
    if hidden_word == guess:
        print("Congrats!! You did it.")
    else:
        result = ""    
        for i,j in zip(guess, hidden_word):
            if i == j:
                result = result + "(C)"
            elif i in hidden_word:
                result = result + "(WP)"
            else:
                result = result + "(NT)"
        print(result)
        return False
    
def main_():
    attempt = 5
    give_instructions( )
    while attempt > 0:
        guess = input("Enter four letter word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1
            print(f"You have {attempt} attempts left")
    else:
        print("GAME OVER")


main_()
