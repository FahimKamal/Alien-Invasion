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

# Register the shapes
window.register_shape('alien_ship2.gif')
window.register_shape('player2.gif')

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
        self.score_turtle = turtle.Turtle()
        self.score_turtle.goto(-200, 290)
        self.score_turtle.speed(0)
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.color('white')

    def draw_border(self):
        """Will draw the border"""
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

    def show_score(self):
        """Will show the score on screen"""
        self.score_turtle.clear()
        self.score_turtle.write(f'Score: {self.score}', align='left', font=('Arial', 18, 'bold'))

    def game_over(self):
        self.score_turtle.clear()
        self.score_turtle.color('red')
        self.score_turtle.goto(0, 0)
        self.score_turtle.write('Game Over', align='center', font=('Arial', 30, 'bold'))
        self.score_turtle.sety(-50)
        self.score_turtle.color('white')
        self.score_turtle.write(f'Final score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def play_sound(self, file_name):
        """Will play sound"""
        winsound.PlaySound(file_name, winsound.SND_ASYNC)

class Player(Base):
    def __init__(self, shape, color, startx, starty):
        Base.__init__(self, shape, color, startx, starty)
        self.left(90)
        self.speed = 15

    def is_collision(self, other):
        """Returns true if two objects crash with each-other"""
        if self.distance(other) < 40:
            return True
        return False

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
            game.play_sound('laser-gun.wav')

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
player = Player('player2.gif', 'blue', 0, -240)
# Create enemy
# enemy = Enemy('circle', 'red', random.randint(-180, 180), random.randint(0, 270))
enemies = [Enemy('alien_ship2.gif', 'red', random.randint(-180, 180), random.randint(0, 270))
           for _ in range(5)]
# Create missile
missile = Missile('triangle', 'yellow', -1000, -1000)
# Create Border
game = Game('triangle', 'white', -200, -275)
game.draw_border()
game.show_score()

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
                game.play_sound('explosion.wav')
                enemy.go_random()
                missile.make_ready()
                game.score += 1
                game.show_score()
        if player.is_collision(enemy):
            game.game_over()
            game.play_sound('Lost_life.wav')
            break
    else:
        time.sleep(0.02)
        continue
    break

while True:
    window.update()
