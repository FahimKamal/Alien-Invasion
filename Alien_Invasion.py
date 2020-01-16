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
window.bgpic('game_bg2.gif')
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

# Scoring system
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color('white')
score_pen.goto(-200, 290)
score_pen.hideturtle()
score_pen.write(f'Score: {score}', font=('Arial', 18, 'bold'))

# Register the sheps
window.register_shape('alien_ship2.gif')
window.register_shape('player2.gif')

# Create player
player = turtle.Turtle()
player.speed(0)
player.color('blue')
player.shape('player2.gif')
player.penup()
player.goto(0, -240)
player.left(90)
# Player speed
player.dx = 10

def create_enemy():
    """Function to create enemies"""
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.color('red')
    enemy.shape('alien_ship2.gif')
    enemy.penup()
    # will pop up in a random location
    enemy.goto(random.randint(-180, 180), random.randint(0, 270))
    # enemy speed
    enemy.dx = 4
    return enemy


# Create the enemy
enemy_number = 5
enemies = [create_enemy() for _ in range(enemy_number)]

# Missile for the player
missile = turtle.Turtle()
missile.speed(0)
missile.color('orange')
missile.shape('triangle')
missile.shapesize(stretch_wid=0.3, stretch_len=0.5)
missile.penup()
missile.left(90)
missile.goto(-1000, -1000)
missile.speed = 20
missile.state = 'ready'


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
    global score
    for enemy in enemies:
        if enemy.xcor() > 190:
            # If enemy reaches the right border it reverses
            # enemy also come down a little bit too
            # All at once
            # for enemys in enemies:
            #     enemys.sety(enemys.ycor() - 20)
            #     enemys.dx *= -1

            enemy.sety(enemy.ycor() - 20)
            enemy.dx *= -1
        elif enemy.xcor() < -190:
            # If enemy reaches the left border it reverses
            # enemy also come down a little bit too
            # All at once
            # for enemys in enemies:
            #     enemys.sety(enemys.ycor() - 20)
            #     enemys.dx *= -1

            enemy.sety(enemy.ycor() - 20)
            enemy.dx *= -1

        # Border checking for missile
        if missile.ycor() > 260:
            missile.state = 'ready'
            missile.goto(-1000, -1000)

        # Check if missile and enemy made a collision
        # If yes then the enemy re-appear in random location.
        if missile.distance(enemy) < 20:
            missile.state = 'ready'
            missile.goto(-1000, -1000)
            enemy.goto(random.randint(-180, 180), random.randint(0, 250))
            score += 1
            score_pen.clear()
            score_pen.write(f'Score: {score}', font=('Arial', 18, 'bold'))
            winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)

        # Check is enemy hits the player
        # If yes then it's game over.
        if player.distance(enemy) < 15:
            winsound.PlaySound('Lost_life.wav', winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print('Game over')
            return True
        enemy.forward(enemy.dx)
    missile.forward(missile.speed)


def fire_missile():
    # Comes to the position of the player
    if missile.state == 'ready':
        missile.goto(player.xcor(), player.ycor())
        missile.state = 'firing'
        winsound.PlaySound('laser-gun.wav', winsound.SND_ASYNC)


# Key binding
window.listen()
window.onkeypress(move_right, 'Right')
window.onkeypress(move_left, 'Left')
window.onkeypress(fire_missile, 'space')

# Main game loop
while True:
    window.update()
    # move the enemy
    end_game = movement()
    time.sleep(0.03)
    if end_game:
        break
