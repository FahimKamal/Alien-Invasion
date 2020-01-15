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
window.tracer(0)

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
# Player speed
player.dx = 10

# Create the enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.color('red')
enemy.shape('square')
enemy.penup()
enemy.goto(-150, 200)
# enemy speed
enemy.dx = 4

# Missile for the player
missile = turtle.Turtle()
missile.speed(0)
missile.color('orange')
missile.shape('triangle')
missile.shapesize(stretch_wid=0.3, stretch_len=0.5)
missile.penup()
missile.goto(-1000, -1000)
missile.speed = 20
missile.left(90)


# Functions
def move_right():
    """Move the player to right"""
    if player.xcor() < 190:
        player.setx(player.xcor() + player.dx)


def move_left():
    """Move the player to left"""
    if player.xcor() > -190:
        player.setx(player.xcor() - player.dx)


def movement():
    """Movement of the enemy and missile will be controlled from here"""
    if enemy.xcor() > 190:
        # If enemy reaches the right border it reverses
        enemy.setx(190)
        enemy.dx *= -1
        # enemy also come down a little bit too
        enemy.sety(enemy.ycor() - 20)
    elif enemy.xcor() < -190:
        # If enemy reaches the left border it reverses
        enemy.setx(-190)
        enemy.dx *= -1
        # enemy also come down a little bit too
        enemy.sety(enemy.ycor() - 20)

    enemy.forward(enemy.dx)
    missile.forward(missile.speed)


def fire_missile():
    # Comes to the position of the player
    missile.goto(player.xcor(), player.ycor())


# Key binding
window.listen()
window.onkeypress(move_right, 'Right')
window.onkeypress(move_left, 'Left')
window.onkeypress(fire_missile, 'space')

# Main game loop
while True:
    window.update()
    # move the enemy
    movement()
    time.sleep(0.05)
