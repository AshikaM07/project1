"""
Number Guessing Game
--------------------
Rules:
- Computer picks a random number between 1 and 100
- You have to guess it
- After each guess, you'll get a hint ("Too High" or "Too Low")
- The game ends when you guess correctly, and it will show your attempts
"""

import random   #random module is imported

def get_guess(): 
    
    while True:
        try:       #try-except for exception handling
            guess = int(input("Enter your guess: ")) 
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number only between 1 and 100")
        except ValueError:
            print("Try again.")

def play_game():
    num = random.randint(1, 100)
    a = 0 # 'a' is the attempts 
    print("\nGuess the number!!")
    while True:
        guess = get_guess()
        a += 1
        if guess < num:
            print("Too Low!")
        elif guess > num:
            print("Too High!")
        else:
            print(f"Correct! You guessed it in {a} tries.") #formatted string
            return a
        
def main():
    best_score = None #the best score set as none
    print("Welcome to the Number Guessing Game!")
    while True:
        
        print("\nMenu:")
        print("1. Play")
        print("2. View Best Score")
        print("3. Exit")

        #above is the menu of the game
        
        ch = input("Choose option: ") #the player needs to choose any one of the options
        if ch == "1":
            score = play_game()
            if best_score is None or score < best_score:
                best_score = score
                print("New Best Score!")
        elif ch == "2":
            if best_score is None:
                print("No games played yet.")
            else:
                print("Best Score: ",best_score," attempts")
        elif ch == "3":
            print("Thank You for Playing!")
            break
        else:
            print("Invalid choice. Please pick from options 1, 2 or 3.") #if the player chooses anything outside the option


main() #calling the main function for the game
