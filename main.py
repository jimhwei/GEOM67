# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# November 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
import csv

user = input("Select turtle object/color: ")

# setting up the turtle
wn = turtle.Screen()
wn.bgcolor("grey")
snake = turtle.Turtle()
snake.shape("turtle")
snake.color("green")
snake.pensize(50)

# how should the user interact with this screen
wn.exitonclick()