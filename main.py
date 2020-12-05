# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# Date Modified December 04, 2020

# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

import turtle
from questions import MultiChoice
from CoinFlip import Coinflip
from dice import diceroll
from rockpaperscissors import rps

def replay():
    print("Would you like to play again?")
    user = input("Y/N:\n>>")
    if user.upper == "Y":
        main()
    else:
        print("See you next time!")

def main():
    # Asks for player name
    Guest = input("\nWelcome to Group 2's Awesome Snakes and Ladders\nI'm Turtles, what's your name? >>")
    print ("Welcome", Guest)
    # Game introduction message
    print("There is a series of questions and 3 minigames")
    print("Help me move through the squares!")
    print("Each correct answer and win in the games moves me forward")
    print("If you fail 3 times then the game is over! GOOD LUCK")

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

    # Game 1
    print()
    MultiChoice()
    user.forward(275)
    user.shapesize(2,2,1)

    print()
    Coinflip()
    user.forward(275)
    user.shapesize(3,3,1)

    print()
    MultiChoice()
    user.right(85)
    user.forward(190)
    user.right(95)
    user.shapesize(4,4,1)

    print()
    diceroll()
    user.forward(275)
    user.shapesize(5,5,1)

    print("\nBONUS QUESTION")
    MultiChoice()
    print("Congrats you move two squares!")
    user.forward(270)
    user.shapesize(6,6,1)

    user.left(80)
    user.forward(190)
    user.left(100)
    user.shapesize(7,7,1)

    print()
    rps()
    user.forward(270)
    user.shapesize(8,8,1)
    
    print()
    MultiChoice()
    user.forward(270)
    user.shapesize(9,9,1)

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

    print("\nCongrats Master", Guest, ", you have beaten the game!")
    print("Click to Exit Game")

    wn.exitonclick()
    replay()

main()