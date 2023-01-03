#MAIN

from turtle import Screen
import time
from clasess_to_import import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

is_true = True
while is_true:
    screen.update()
    time.sleep(0.1)
    is_true = snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 298 or snake.segments[0].ycor() < -295:
        scoreboard.game_over()
        is_true = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_true = False
            scoreboard.game_over()


screen.exitonclick()


#FOOD

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)



#SCOREBOARD

from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=('Arial', 14, 'normal'))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



#CLASSESS_TO_IMPORT

from turtle import Turtle
from scoreboard import Scoreboard

START = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in START:
            self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

        '''if self.segments[0].xcor() > 280 or self.segments[0].xcor() < -280 or self.segments[0].ycor() > 298 or self.segments[0].ycor() < -295:
            Scoreboard.game_over(self)
            return False
        else:'''
        return True

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)


