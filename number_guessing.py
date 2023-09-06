'''Number guessing using Random Module'''
import random

# initialize number of tries
tries = 1

# intialize flag
flag = 0

# take range input
print("\nEnter a range\n")
a = int(input("Enter lower limit\n"))
b = int(input("\nEnter upper limit\n"))

# generate a random number
random_num = random.randint(a,b)

# guess number input
guess_num = int(input("\nNow, make a guess\n"))


'''Function to display correct guess'''
def correct_guess(tries):
    print("\nCongratulations! You guessed right in ",tries,"tries")


'''Function to take user choice'''
def user_choice():
    choice = int(input("\nPress 1 to try again.\nPress 2 to take a hint.\nPress 3 to Exit.\n"))
    if choice in range(1,4):
        return choice
    else:
        print("\nWrong choice")
    
    return user_choice()


# display correct guess if user got it right in the first try
if guess_num == random_num:
    correct_guess(tries)
    flag = 1

# prompt for user choice if user got it wrong in the first try
while flag != 1:
    print("\nMmm...That's Wrong!")
    x = user_choice()

    # ask for user choice until either the user chooses to exit or makes the orrect guess
    while (x != 3):
        # try again
        if x == 1:
            guess_num = int(input("\nMake another guess\n"))
            tries+=1

            # break from the loop in case of correct guess
            if guess_num == random_num:
                correct_guess(tries)
                flag=1
                break
            else:
                # wrong choice
                print("That's quite wrong!")
                # prompt for making a choice again
                x = user_choice()

        # take hint
        elif x == 2:
            print("\nYOUR HINT: ")
            
            if guess_num not in range(a,b+1):
                print("\nYour guess is out of range")
            elif guess_num > random_num:
                print("\nYour guess is too big")
            elif guess_num < random_num:
                print("\nYour number is too small")
            
            #prompt for making a choice again
            x = user_choice()
        
    # if user chooses to exit
    flag = 1
