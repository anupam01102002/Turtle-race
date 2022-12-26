from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

colours = ["red", "blue", "orange", "yellow", "purple", "green"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: (red, blue, orange, yellow, purple, green) ")
Y_positions = [-75, -45, -15, 15, 45, 75]
all_turtle = []

for turtle_index in range(0,6):
    tim = Turtle(shape = "turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x = -230 , y =Y_positions[turtle_index])
    all_turtle.append(tim)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtles in all_turtle:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You have Won! The {winning_color} Turtle is the Winner")
            else:
                print(f"You have Lost! The {winning_color} Turtle is the Winner")

        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)

screen.exitonclick()