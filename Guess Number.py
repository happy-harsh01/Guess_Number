import random

print("=====Welcome to Guess number Game=====\nYou have to guess the hidden number\nType any number between 1 and 100")
num = random.randint(1, 101)
guesses = 0
while True:
    if guesses == 10:
        print("You lose you consumed all 10 guesses.")
        exit()
    try:
        a = int(input("Enter your choice : "))
        if a > 100:
            print("Please give a valid number between 1 and 100")
        elif a == num:
            print("Wow you guessed it right!")
            print(f"Your score is : {guesses}")
            with open("GuessScore.txt", 'r') as f:
                hi_score = f.read()
            if int(hi_score) > guesses:
                print("You broke the hi score.")
                with open("GuessScore.txt", 'w') as f:
                    f.write(str(guesses))
            else:
                print("You didn't break the hi score.")
            break
        elif a < num:
            print("You guessed it wrong. Guess a big number.")
        elif a > num:
            print("You guessed it wrong. Guess a small number.")
    except ValueError:
        print("Please enter a number between 1 and 100.")
    guesses += 1
