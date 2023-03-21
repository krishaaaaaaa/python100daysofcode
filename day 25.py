from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('U.S. States')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
turtl = Turtle()
turtl.hideturtle()
turtl.penup()
guesses = 0
list_of_answers = []
data = pandas.read_csv('50_states.csv')
list_of_state = data.state.to_list()
while len(list_of_answers)<50:

    answer = screen.textinput(title=f'{guesses}/50 Guess', prompt=f"What's your guess?")

    right = data[data.state == answer.title()]

    list_of_answers.append(answer.title())
    if answer.title() == 'Exit':
        break
    for ans in list_of_state:
        if ans != answer.title() or list_of_answers.count(ans)>1:
            continue
        else:
            print(ans)
            guesses += 1
            xc = int(right.x.values)
            yc = int(right.y.values)
            print(xc, yc)
            turtl.setpos(xc, yc)
            turtl.write(answer, font=('arial', 8, 'normal'))


'''def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()'''





#50_states.csv
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
Arkansas,57,-53
California,-297,13
Colorado,-112,20
Connecticut,297,96
Delaware,275,42
Florida,220,-145
Georgia,182,-75
Hawaii,-317,-143
Idaho,-216,122
Illinois,95,37
Indiana,133,39
Iowa,38,65
Kansas,-17,5
Kentucky,149,1
Louisiana,59,-114
Maine,319,164
Maryland,288,27
Massachusetts,312,112
Michigan,148,101
Minnesota,23,135
Mississippi,94,-78
Missouri,49,6
Montana,-141,150
Nebraska,-61,66
Nevada,-257,56
New Hampshire,302,127
New Jersey,282,65
New Mexico,-128,-43
New York,236,104
North Carolina,239,-22
North Dakota,-44,158
Ohio,176,52
Oklahoma,-8,-41
Oregon,-278,138
Pennsylvania,238,72
Rhode Island,318,94
South Carolina,218,-51
South Dakota,-44,109
Tennessee,131,-34
Texas,-38,-106
Utah,-189,34
Vermont,282,154
Virginia,234,12
Washington,-257,193
West Virginia,200,20
Wisconsin,83,113
Wyoming,-134,90
