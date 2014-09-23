import random

# Asks the user for guesses until a correct guess is made or 5 wrong
# guesses have been made. Gives hints after each wrong guess.

def game():
    secret_number = random.choice(range (1, 11))

    i = 5
    while i > 0:
        guess = int(input('Guess a number between 1 and 10: '))

        diff = abs(guess - secret_number)
        if diff == 0:
            break
        elif diff > 5:
            print('not even close')
        elif diff >= 3:
            print('close')
        else:
            print('almost there')
        i -= 1  

    if i != 0:
        print("You guessed the right number!")
    else:
        print("You lost the game.")

def main():
    game()

if __name__ == '__main__':
    main()
