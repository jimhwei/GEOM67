# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv
import random
from questions import questions
from CoinFlip import Coinflip
from dice import diceroll
from rockpaperscissors import rps
import time

# Game introduction message

print("Welcome to Group 2's Awesome Snakes and Ladders")
print("There is series of questions are 3 minigames ")
print("Each correct answer and win in the games moves you forward")
### Ask for player name
Guest = input("Im Turtles, what's your name?" :)
print ("Welcome", Guest)

#Background image
screen = turtle.Screen()
screen.setup(900,600)
screen.bgpic('boardgamegrid-01.png')


# user = input("Select turtle object/color: ")

# setting up the turtle
wn = turtle.Screen()
# background change
# wn.bgcolor("grey")
# user gets to choose shapes
# turtle.getshapes()

# initiate turtle
user = turtle.Turtle()
user.penup()
user.goto(-275,185)
user.shape("turtle")
user.color("green")

###############################################

# coin flip game

# game1 = input("True")
# if game1 == "True":
#     user.forward(180)

# how should the user interact with this screen
# it should be intermediate inputs

# questions()

#input()

user.forward(275)
user.shapesize(2,2,1)

#input()

user.forward(275)
user.shapesize(3,3,1)

#input()
# Coinflip()
user.right(85)
user.forward(190)
user.right(95)
user.shapesize(4,4,1)

#input()
# user.right(2)
user.forward(275)
# user.left(2)
user.shapesize(5,5,1)

#input()
# diceroll()
# user.right(2)
user.forward(270)
# user.left(2)
user.shapesize(6,6,1)

#input()
user.left(80)
user.forward(190)
user.left(100)
user.shapesize(7,7,1)

#input()
# rps()
# user.left(2)
user.forward(270)
# user.right(2)
user.shapesize(8,8,1)

#input()
# user.left(2)
user.forward(270)
# user.right(2)
user.shapesize(9,9,1)

<<<<<<< HEAD

screen.update()
screen.bgpic('victory-01.png')

user.left(90)
user.forward(360)
user.left(90)
user.forward(540)
user.left(90)
user.forward(360)
user.left(90)
user.forward(900)


print("Victory!")
=======
print("Congrats Master", Guest)
>>>>>>> 3c0c829a45703472ab95d374ea1cb7060488de6d
print("Click to Exit Game")

wn.exitonclick()