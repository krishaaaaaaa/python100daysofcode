#SCOREBOARD

from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270,270)
        self.write(f'Level:{self.level}', align= 'left', font=FONT)

    def inc_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level:{self.level}', align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)


#CAR_MANAGER

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create(self):
        random_chance = random.randint(1,7)
        if random_chance == 5:

            new_car = Turtle('square')

            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_pos = random.randint(-240, 240)
            new_car.goto(300, y_pos)
            self.car_list.append(new_car)
        else: pass

    def movement(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


#PLAYER

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.shape('turtle')

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

#MAIN

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create()
    cars.movement()


    for car in cars.car_list:
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False


    if player.finish():
        player.go_to_start()
        cars.level_up()
        scoreboard.inc_level()


screen.exitonclick()



