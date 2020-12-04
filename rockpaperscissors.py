#Jeonghyeok Seo
#Rock Paper Scissors minigame
#get user random selection Rock, Paper, or Scissors
#get computer's random selection Rock, Paper, or Scissors
#compare to computer choice
#turtle moves forward if user wins

      
#Options of Rock, Paper and Scissors

options = ["Rock", "Paper", "Scissors"]

#Get user selection

user = input("Please choose one form Rock, Paper, and Scissors :")
user = user.capitalize()
print("Player's Choice", user)

#Error handling when user input other value
while user.capitalize() not in options:
   print("Incorrect input. Please enter Rock, Paper, or Scissors")
   user = input("Please choose one form Rock, Paper, and Scissors:" )
   user = user.capitalize()
   print("Player's Choice", user)

#Computer choose one value randomly

import random
Computer = random.choice(options)
print("Computer's choice", Computer)

#Compare the values
winner = None

#When Computer select Rock
if Computer == "Rock":
   if user == "Scissors":
      winner = "Computer"
   elif user == "Paper":
      winner = "user"   
   else:
      winner == None


#When Computer select Paper
elif Computer == "Paper":
   if user == "Rock":
      winner = "Computer"
   elif user == "Scissors":
      winner = "user"
   else:
      winner == None  

#When Computer select Scissors
else: 
   if user == "Paper":
      winner = "Computer"
   elif user == "Rock":
      winner = "user"
   else:
      winner == None

#Print the resaults
if winner == "Computer" :
   print("You lose")
elif winner == "user":
   print("You win!")
else:
   print("Ties")