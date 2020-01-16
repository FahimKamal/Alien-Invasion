"""
Alien Invasion 2.0 (with class)
Created by: Fahim kamal
Date: 17.01.2020
"""
import turtle, random, time, winsound

# Setup the window
window = turtle.Screen()
window.setup(width=500, height=650)
window.bgcolor('black')
window.bgpic('game_bg2.gif')
window.title('Alien Invasion by Fahim Kamal')
window.tracer(0)

# Base class
class Base(turtle.Turtle):
    def __init__(self, shape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=shape)
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(startx, starty)
        self.speed = 1

# Game class
class Game(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)
        self.score = 0

    def draw_border(self):
        self.pensize(4)
        self.pendown()

        for i in range(4):
            if i % 2:
                self.forward(550)
            else:
                self.forward(400)
            self.left(90)

        self.penup()
        self.hideturtle()

class Player(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)
        self.left(90)
        self.speed = 5

    def move_left(self):
        """Move the player to left"""
        self.setx(self.xcor() - self.speed)

    def move_right(self):
        """Move the player to left"""
        self.setx(self.xcor() + self.speed)


class Enemy(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)

# Create Player
player = Player('triangle', 'blue', 0, -240)
# Create Border
game = Game('triangle', 'white', -200, -275)
game.draw_border()

# Key binding
window.listen()
window.onkeypress(player.move_left, 'Left')
window.onkeypress(player.move_right, 'Right')

# Main game loop
while True:
    window.update()