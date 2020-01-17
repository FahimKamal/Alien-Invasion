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

    def is_collision(self, other):
        """Returns true if two objects crash with each-other"""
        if self.distance(other) < 20:
            return True
        return False

    def go_random(self):
        self.goto(random.randint(-180, 180), random.randint(0, 270))


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
        self.speed = 15

    def move_left(self):
        """Move the player to left"""
        self.setx(self.xcor() - self.speed)

    def move_right(self):
        """Move the player to left"""
        self.setx(self.xcor() + self.speed)


class Enemy(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)
        self.speed = 4

    def move(self):
        """Movement of the object will be controlled from here"""
        self.forward(self.speed)

        # Border check
        if self.xcor() > 190:
            # If hit the right border reverse direction
            # Also comes 1 step downward
            self.sety(self.ycor() - 20)
            self.setx(190)
            self.speed *= -1
        if self.xcor() < -190:
            # If hit the left border reverse direction
            # Also comes 1 step downward
            self.sety(self.ycor() - 20)
            self.setx(-190)
            self.speed *= -1

class Missile(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)
        self.speed = 5
        self.left(90)
        self.shapesize(stretch_wid=0.4, stretch_len=0.5)
        self.state = 'ready'

    def fire(self):
        if self.state == 'ready':
            self.goto(player.xcor(), player.ycor())
            self.state = 'firing'

    def make_ready(self):
        """Make the missile ready to fire again"""
        self.goto(-1000, -1000)
        self.state = 'ready'

    def move(self):
        self.forward(self.speed)

        # Top border check
        if self.ycor() > 260:
            self.make_ready()


# Create Player
player = Player('triangle', 'blue', 0, -240)
# Create enemy
# enemy = Enemy('circle', 'red', random.randint(-180, 180), random.randint(0, 270))
enemies = [Enemy('circle', 'red', random.randint(-180, 180), random.randint(0, 270))
           for _ in range(5)]
# Create missile
missile = Missile('triangle', 'yellow', -1000, -1000)
# Create Border
game = Game('triangle', 'white', -200, -275)
game.draw_border()

# Key binding
window.listen()
window.onkeypress(player.move_left, 'Left')
window.onkeypress(player.move_right, 'Right')
window.onkeypress(missile.fire, 'space')

# Main game loop
while True:
    window.update()
    # Move the enemies
    for enemy in enemies:
        enemy.move()
        if missile.state == 'firing':
            missile.move()
            if missile.is_collision(enemy):
                enemy.go_random()
                missile.make_ready()
    time.sleep(0.02)
