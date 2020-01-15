"""
Alien Invasion
Created by: Fahim Kamal
Date: 14.01.2020
"""
import turtle
import random
import time
import winsound

# Setup the window
window = turtle.Screen()
window.setup(width=500, height=650)
window.bgcolor('black')
window.title('Alien Invasion by Fahim Kamal')
window.tracer()

# Draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.goto(-200, -275)
border_pen.pensize(4)
border_pen.pendown()

for i in range(4):
    if i % 2:
        border_pen.forward(550)
    else:
        border_pen.forward(400)
    border_pen.left(90)

border_pen.penup()
border_pen.hideturtle()

# Create player
player = turtle.Turtle()
player.speed(0)
player.color('blue')
player.shape('triangle')
player.penup()
player.goto(0, -265)
player.left(90)
player.distance = 10


# Functions
def move_right():
    player.setx(player.xcor() + player.distance)


def move_left():
    player.setx(player.xcor() - player.distance)


# Key binding
window.listen()
window.onkeypress(move_right, 'Right')
window.onkeypress(move_left, 'Left')

# Main game loop
while True:
    window.update()
