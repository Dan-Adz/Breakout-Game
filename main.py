# Breakout Game

import time
from turtle import Screen
from player import Player
from blocks import Blocks
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

player = Player()
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, 'd')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect if ball hits a wall
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce_x()
    # Detect if ball hits the top of the window
    if ball.ycor() > 270:
        ball.bounce_y()
    # Detect if ball goes under paddle(game over)
    if ball.ycor() < -280:
        scoreboard.game_over()
        break
        # Detect where the ball hits the player
    if ball.distance(player) < 110 and ball.ycor() < -250:
        if player.xcor() > 0:
            if ball.xcor() > player.xcor():
                ball.bounce_x()
            else:
                ball.bounce_y()
        elif player.xcor() < 0:
            if ball.xcor() < player.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()
        else:
            if ball.xcor() > player.xcor():
                ball.bounce_x()
                ball.bounce_y()
            elif ball.xcor() < player.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()
    # Detect collision with blocks
    for block in blocks.blocks:
        if ball.distance(block) < 40:
            block.quantity -= 1
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            if block.quantity == 0:
                block.clear()
                block.goto(3000, 3000)
                blocks.blocks.remove(block)
            if ball.xcor() < block.left_wall:
                ball.bounce_x()
            elif ball.xcor() > block.right_wall:
                ball.bounce_x()
            elif ball.ycor() < block.bottom_wall:
                ball.bounce_y()
            elif ball.ycor() > block.upper_wall:
                ball.bounce_y()
    if len(blocks.blocks) == 0:
        scoreboard.game_over()

screen.exitonclick()
