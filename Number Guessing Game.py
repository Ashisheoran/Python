import random

def no_guessing_game():
    number = random.randint(1,100)
    attempts = 0 

    print("\n.......Welcome to Number Guessing Game.......\n")
    while True:
        try:
            if attempts == 5:
                print("You Loose the game... Your Attempts are Over..")
                print(f"........ The number is {number} .......")
                break
            user_input = int(input("Enter Your Guessing Number: "))
            attempts += 1
            if user_input < number:
                print("Your Number is Low.... Try Again..!\n")
            elif user_input > number:
                print("Your Number is High.... Try Again..!\n")
            else:
                print(f"Congratulation... You Guess the Number in {attempts} attempt")
                break
           
        except ValueError:    
            print("Please Enter a Valid Number")


no_guessing_game()