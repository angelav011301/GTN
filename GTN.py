import random
def intro():
    print("Welcome to Guess The Number Game!")
# guessesTaken = 0
# print("Guess the number from 1-25")
# number = random.randint(1,25)
    print("You'll have 5 chances to guess the number from 1-25, good luck :)")
    print("Also, you may choose 1 and 25 as a guess.")

# if guess > 25:
#     print ("Not a valid choice, try again")
#
# if guess < 1:
#     print ("Not a valid choice, try again")
# guess = input()
# guess = int(guess)

def game():
    guess = input()
    guess = int(guess)
    guessesTaken = 0
    number = random.randint(1,25)
    while guessesTaken < 5:
        print ('Pick a number')
        # guess = input()
        # guess = int(guess)

        guessesTaken = guessesTaken + 1
        #guessesTaken =+ 1
        return
def checkInputValid():
    if guess > 25:
        print ("Not a valid choice, try again")
    else:
        guess < 1
        print ("Not a valid choice, try again")

def checkNumberValue():
    if guess < number:
        print('Your guess is to low.')
    elif guess > number:
        print('Your guess is to high.')
    else:
        # guess == number
        # quit()

            def outcome():
                if guess == number:
                    guessesTaken = str(guessesTaken)
                    print('Good Job')
                    begin()
                else:
                    guess != number
                    number=str(number)
                    print('Nope, Try again')
                    begin()

def begin():
    while True:
        restart = input('do you want to restart yes/no?')
        if restart == 'no':
            exit()
        else:
            restart == 'yes'

def main():
    intro()
    checkInputValid()
    checkNumberValue()
    game()
    outcome()

#-------------------------------------------------------------------
if __name__ == "__main__":
    main()
