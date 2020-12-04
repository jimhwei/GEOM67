#Jenn Debono
#dice roll game
#get user random selection from 1 to 6, like a 6-sided dice
#compare to computer random choice
#if user and computer choice match or is higher than computer choice, user wins
#turtle moves forward if user wins
#invalid inputs: integers less than 0 or greater than 7, negative integers,
# and string values
#play continues until user wins

#import random module 
import random

#user defined function for game
def diceroll():

    # start of error handling 
    try:
        # create a die
        dice = [1,2,3,4,5,6]

        #get user selection from 1 to 6
        playerRoll = int(input("Choose a number between 1 and 6: "))
        print("Player Choice: ", playerRoll)
  
        # error handling for user entry of value other than the list from 1-6
        while playerRoll not in dice:
            print ("Incorrect numeric value. Please enter a number between 1 and 6")
            # send user back to enter input
            playerRoll = int(input("Choose a number between 1 and 6: "))
            print("Player Choice: ", playerRoll)
    
        #computer random roll
        dice_outcome = random.choice(dice)
        print("Computer Choice: ", dice_outcome)
        print()
    
        #final output to determine win and loss
        #win scenario 1: guess number higher than computer
        if dice_outcome < playerRoll:
            print ("You guessed a higher number than the computer! You Win!")
        #win scenario 2: match same number as computer
        elif dice_outcome == playerRoll:
            print ("You matched the computer! Great guess! You Win!")
        #loss scenario: computer select number higher than user
        else:
            print ("Computer Wins. Try Again")

    # error handling for string entries 
    except ValueError:
        print ("Oops! Letters are not going to work here. Try again")
        # send user back to enter input
        diceroll()

# game function call  
# diceroll()