from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
my_screen = Screen()
my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
my_screen.title("Turtle race")

SCREEN_LEFT_LIMIT = SCREEN_WIDTH / 2 * -1 + 10
SCREEN_RIGHT_LIMIT = SCREEN_WIDTH / 2 - 30
DISTANCE_BETWEEN_TURTLES = 20

colors = ["red", "blue", "yellow", "green", "orange", "purple"]
turtles = []

user_choice = my_screen.textinput(title="What turtle would win?", prompt="Choose your turtle color")


def create_turtles():
    for index in range(len(colors)):
        current_turtle = Turtle(shape="turtle")
        current_turtle.penup()
        current_turtle.color(colors[index])
        turtles.append(current_turtle)


def position_turtles():
    for index in range(len(colors)):
        turtles[index].goto(x=SCREEN_LEFT_LIMIT, y=-80 + (40 * index))


def race():
    race_is_on = True
    while race_is_on:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.position()[0] >= SCREEN_RIGHT_LIMIT:
                print(f"Winner is {turtle.color()[0]}")
                if turtle.color()[0] == user_choice:
                    print("You have won the prize!")
                else:
                    print(f"Sorry you bet for turtle {user_choice}. Better luck next time!")
                race_is_on = False
                break




print(f"User has bet turtle {user_choice} would win")

create_turtles()
position_turtles()

race()


my_screen.exitonclick()




