# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv
import random
from questions import questions

# Game introduction message

print("Welcome to Group 2's Awesome Snakes and Ladders")


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

# initiate turtle
user = turtle.Turtle()
user.penup()
user.goto(-180,120)
user.shape("turtle")
user.color("green")

###############################################

# coin flip game

# game1 = input("True")
# if game1 == "True":
#     user.forward(180)

# how should the user interact with this screen
# it should be intermediate inputs

questions()

user.forward(275)
user.shapesize(2,2,1)

user.forward(275)
user.shapesize(3,3,1)

questions()

user.right(90)
user.forward(170)
user.right(90)
user.shapesize(4,4,1)

user.right(2)
user.forward(275)
user.left(2)
user.shapesize(5,5,1)

questions()
user.right(2)
user.forward(290)
user.left(2)
user.shapesize(6,6,1)

user.left(70)
user.forward(190)
user.left(110)
user.shapesize(7,7,1)

questions()
user.left(2)
user.forward(270)
user.right(2)
user.shapesize(8,8,1)

user.left(2)
user.forward(250)
user.right(2)
user.shapesize(9,9,1)


wn.exitonclick()

print("Victory!")