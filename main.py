# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv
<<<<<<< HEAD
#Background image
screen = turtle.Screen()
screen.setup(900,600)
screen.bgpic('boardgamegrid-01.png')
screen.update()

=======
import random
>>>>>>> 6e1934f63d3171a0a0e9ef290f96382a33bf7721

#Background image
screen = turtle.Screen()
screen.setup(900,600)
screen.bgpic('boardgamegrid-01.png')
screen.update()

# user = input("Select turtle object/color: ")

# setting up the turtle
wn = turtle.Screen()
# background change
# wn.bgcolor("grey")
# user gets to choose shapes
# turtle.getshapes()

<<<<<<< HEAD
snake = turtle.Turtle()
snake.penup()
snake.goto(-300,120)
snake.shape("turtle")
snake.color("green")

# game 1 input and output
game1 = input("True")
if game1 == "True":
    snake.forward(180)

#kedie tryna commit*
#Test 
# # how should the user interact with this screen
# # it should be intermediate inputs
=======
# initiate turtle
user = turtle.Turtle()
user.penup()
user.goto(-300,120)
user.shape("turtle")
user.color("green")

###############################################

# coin flip game

# game1 = input("True")
# if game1 == "True":
#     user.forward(180)

# how should the user interact with this screen
# it should be intermediate inputs
<<<<<<< HEAD
>>>>>>> 6e1934f63d3171a0a0e9ef290f96382a33bf7721
wn.exitonclick()
=======
wn.exitonclick()
>>>>>>> 183e80ea2f9aff17a201441d056be362ce156967
