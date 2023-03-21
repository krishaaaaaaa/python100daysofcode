#MAIN PONG

import time
from turtle import Turtle, Screen
from Paddle import PaddleFunc
from Ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = PaddleFunc()
l_paddle.create((-380, 0))

r_paddle = PaddleFunc()
r_paddle.create((380, 0))

ball = Ball()
ball.create()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.p_up, 'Up')
screen.onkey(l_paddle.p_down, 'Down')
screen.onkey(r_paddle.p_up, 'w')
screen.onkey(r_paddle.p_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.movement()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    if ball.xcor()> 355 and ball.distance(r_paddle) <50 or ball.xcor()< -355 and ball.distance(l_paddle) <50:
        ball.bounce_x()

    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.r_scored()

    elif ball.xcor() < -385:
        ball.reset_position()
        scoreboard.l_scored()

screen.exitonclick()




#PADDLE


from turtle import Turtle
X = 372
Y = 0


class PaddleFunc(Turtle):

    def create(self,position):
        self.color('white')
        self.shape('square')
        self.shapesize(4, 1)
        self.penup()
        self.goto(position)

    def p_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def p_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(),new_y)
        
        
        
        


#BALL
import random
from turtle import Turtle

ANGLES = [45,135,225,315]

class Ball(Turtle):

    def create(self):
        self.shape('circle')
        self.shapesize(1)
        self.goto(0,0)
        self.color('white')
        self.x_change = 10
        self.y_change = 10

    def movement(self):
        self.setheading(random.choice(ANGLES))
        self.penup()
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x,new_y)

        if self.xcor()>380:
            return ('You Won')
        elif -380>self.xcor():
            return ('You Lose')

    def bounce_y(self):
        self.y_change *= -1

    def bounce_x(self):
        self.x_change *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_change *= -1
        
        
#SCOREBOARD

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(f'{self.r_score}', align='right', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(f'{self.l_score}', align='left', font=('Courier', 80, 'normal'))

    def r_scored(self):
        self.r_score += 1
        self.update()
    def l_scored(self):
        self.l_score += 1
        self.update()


