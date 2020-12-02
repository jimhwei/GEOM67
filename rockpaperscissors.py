# Rock Paper Scissors Mini Game
# Created By: IPGRP2 - J. Seo
# December 2020

#Greeting
print("Welcome to Rock Paper Scissors Mini Game")

#user choose one value

user = input("Please choose one form Rock, Paper, and Scissors :" )
user = user.capitalize()
print(user)


#Computer choose one value randomly


import random
Computer = random.choice(["Rock","Paper","Scissors"])
print(Computer)

#Compare the values
winner = None
if Computer == "Rock":
    if user == "Scissors":
       winner = "Computer"
    elif user == "Paper":
       winner = "user"   
    else:
       winner == None  

elif Computer == "Paper":
    if user == "Rock":
      winner = "Computer"
    elif user == "Scissors":
      winner = "user"
    else:
       winner == None  

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