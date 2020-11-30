# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv
import random

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
wn.exitonclick()
