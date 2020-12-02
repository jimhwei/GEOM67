#CoinFlip
#coin flip
import random
Heads = 0
Tails = 0
# get player to enter choice
######## i intially had this sentence below as int(input....because the computer wil be entering a random int as well but its i
# us rejecting it)
playerChoice = input("Please enter your choice between 1 and 4")
print("playerChoice", playerChoice)
##### the first one i tried the computer was always winning!
#ask computer to flip
computerflip = random.randint
print("computerflip:",computerflip)

if  computerflip <= playerChoice :
    print("You win! move on to the next level!")

elif computerflip == playerChoice :
    print("You win, move on to the next level!")
else:
    print("computer wins!, play again!")


print ("The End")   