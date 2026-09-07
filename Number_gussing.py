def type_text(text):
    for letter in text:
        print(letter,end="",flush=True)
        time.sleep(0.05)
    print()
def rules_display():
        type_text("\nWinning Rules")
        time.sleep(0.3)
        type_text("\n1.Computer generates a random number between 1 and 100.")
        time.sleep(0.3)
        type_text("\n2.User has a maximum of 7 attempts to guess the number.")
        time.sleep(0.3)
        type_text("\n3.User wins immediately if the guess matches the randomly generated number.")
        time.sleep(0.3)
        type_text("\n4.If the guess is lower than the selected number, the program displays \"Too Low\" and the user should try a higher number.")
        time.sleep(0.3)
        type_text("\n5.If the guess is higher than the selected number, the program displays \"Too High\" and the user should try a lower number.")
        time.sleep(0.3)
        type_text("\n6.Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.")
        time.sleep(0.3)
        type_text("\n7.If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.")
        time.sleep(0.3)
        print()
def play_game(number,attempt=1):
    if attempt>attempts:
        print("OUT OF ATTEMPTS")
        print("========GAME OVER========")
        return
    else:
        print(f"Attempt-{attempt}/{attempts}:")
        guess=(input("ENTER NUMBER:"))
        if guess.isdigit()==True:
            guess=int(guess)
            if guess>100 or guess<1:
                print()
            elif guess==number:
                print("Correct Answer")
                print(f"You Guessed in {attempt} attempts")
                print("========You Won The Game========")
            else:
                if guess<number:
                    print("TOO LOW,Guess Higher Number")
                    play_game(number,attempt+1)
                else:
                    print("TOO High,Guess Lower Number")
                    play_game(number,attempt+1)
        else:
            print("Enter Valid Input")
            play_game(number,attempt)
import random
import time
a=random.randint(1,100)
attempts=7
print("==Welcome to Number Guessing Game==")
rules_display()
play_game(a)