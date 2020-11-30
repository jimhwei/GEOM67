# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv

# user = input("Select turtle object/color: ")

# setting up the turtle
wn = turtle.Screen()
wn.bgcolor("grey")
# turtle.getshapes()

# initiate turtle
user = turtle.Turtle()
user.penup()
user.goto(-350,350)
user.shape("turtle")
user.color("green")

# coin flip game

# create a die
die = [1,2,3,4,5,6]

game1 = input("True")
if game1 == "True":
    user.forward(180)

# how should the user interact with this screen
# it should be intermediate inputs
wn.exitonclick()