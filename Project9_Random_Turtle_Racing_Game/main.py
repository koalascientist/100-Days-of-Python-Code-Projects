from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Choose one of the "
                                                              "following colors: red, orange, yellow, green, blue or "
                                                              "purple: ")
user_bet = user_bet.lower()

colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

is_race_on = False

if user_bet in colors:
    is_race_on = True
    initial_x_coordinate = -230
    initial_y_coordinate = -100
    height_space = 40
    for turtle_count in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_count])
        new_turtle.penup()
        new_turtle.goto(x=initial_x_coordinate, y=initial_y_coordinate)
        initial_y_coordinate += height_space
        all_turtles.append(new_turtle)
else:
    print("You entered a color which is not valid for this race.")

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
