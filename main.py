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

snake = turtle.Turtle()
snake.penup()
snake.goto(-350,350)
snake.shape("turtle")
snake.color("green")

# game 1 input and output
game1 = input("True")
if game1 == "True":
    snake.forward(180)

# # how should the user interact with this screen
# # it should be intermediate inputs
wn.exitonclick()