#Lets play coin flip!
# player vs computer
import random 
def Coinflip() :

    flip = True

    while flip == True:
        playerflip = int(input("Please enter your choice between 1 and 2"))
        print("playerChoice", playerflip)
        ##Computer choice
        computerflip = random.randint(1,2)
        print("computerflip:", computerflip)
    #play chooses heads, computer chooses heads
        if  playerflip == 1 and  computerflip == 1:
            print("Heads! Proceed to next level!")

    #player Chooses head, computer chooses tail
        elif playerflip == 1 and  computerflip == 2:
            print("You both win move on to next level!")

    #player chooses tail, computer chooses tails
        elif playerflip == 2 and  computerflip == 1:
            print("Tails, Computer wins!")  
          
  
    # player chooses tails, computer chooses tails
        elif playerflip == 2 and  computerflip == 2:
            print("Tails, Computer wins!") 

        
# except ValueError:
#          print ("that is not a valid choice, please flip again") 

    # while True:
    #     print()

    # end = input("Do you want to stop playing (Y/N)? ")
    # print()
    # if  end == 'y' :
    #   break    

if __name__ == "__main__":
    Coinflip()
#    