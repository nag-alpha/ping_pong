from turtle import Screen
from elements import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = PongBall()
scoreboard = Score()


screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.04)
    ball.move()
    scoreboard.show_scores()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() == 330 and ball.distance(r_paddle) < 50 or ball.xcor() == -330 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()
        continue

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.update_score_right()
        ball.color("red")

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.update_score_left()
        ball.color("red")

screen.exitonclick()
