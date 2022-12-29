import random
class CreateDots:

    def dots(self,timmy):
        k = 20
        while k>0:
            a = random.choice(['red','blue', 'lawn green','maroon' ,'yellow', 'gray', 'burlywood', 'tomato', 'slate blue', 'orchid'])
            timmy.dot(10,a)
            timmy.penup()
            timmy.forward(20)

            k -= 1


    def turn(self,timmy):
        timmy.dot(10)
        timmy.left(90)
        timmy.forward(20)
        timmy.left(90)

    def turntwo(self,timmy):
        timmy.dot(10)
        timmy.right(90)
        timmy.forward(20)
        timmy.right(90)




#MAIN
from turtle import Turtle,Screen
import random
from clasess_to_import import CreateDots

timmy = Turtle()
tim = CreateDots()
timmy.shape('turtle')
t = 5
while t>0:
    tim.dots(timmy)
    tim.turn(timmy)
    tim.dots(timmy)
    tim.turntwo(timmy)

    t -= 1
screen = Screen()
screen.exitonclick()


