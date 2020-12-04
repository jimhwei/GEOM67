#Jenn Debono
#dice roll game
#get user random selection from 1 to 6
#compare to computer choice
#if user and computer choice match, user wins
#turtle moves forward if user wins

import random
#import turtle

def diceroll():
#while   
    try:
        # create a die
        dice = [1,2,3,4,5,6]

        #get user selection from 1 to 6
        playerRoll = int(input("Choose a number between 1 and 6: "))
        print("Player Choice: ", playerRoll)
  
        # error handling for uder entry of value higher than 6 
        while playerRoll not in dice:
            print ("Incorrect numeric value. Please enter a number between 1 and 6")
            playerRoll = int(input("Choose a number between 1 and 6: "))
            print("Player Choice: ", playerRoll)
    
        #computer random roll
        dice_outcome = random.choice(dice)
        print("Computer Choice: ", dice_outcome)
        print()
        
    
#############################################################
#Output:
    # if playerRoll > 6:
    #     print ("Incorrect guess. Please enter a number between 1 and 6")
        if dice_outcome <= playerRoll:
            print ("You guessed a higher number than the computer! You Win!")
        elif dice_outcome == playerRoll:
            print ("You matched the computer! Great guess! You Win!")
        else:
            print ("Computer Wins. Try Again")
                
    except ValueError:
        print ("Oops! Letters are not going to work here. Try again")

diceroll()