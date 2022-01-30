# import colorgram
#
# # Extract colors from an image
# colors = colorgram.extract("image.jpg", 50)
#
# # Extract rgb tuples for each color from the image and save it in a list
# color_list = []
# for index in range(len(colors)-1):
#     rgb_color = tuple(colors[index].rgb)
#     color_list.append(rgb_color)
# print(color_list)

# Color palette extracted with the help of the functions above
color_rgb_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
                  (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
                  (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90),
                  (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109),
                  (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210),
                  (77, 37, 76), (120, 117, 155)]

# Requirements:
# 1. Paint 10x10 rows of spots.
# 2. Each of the dots should have size 20 and spaced apart by 50 spaces.
from turtle import Turtle, Screen


def draw_dot_with_trailing_space(turtle_object, dot_size, trailing_space_size):
    turtle_object.dot(size = dot_size)
    turtle_object.penup()
    turtle_object.forward(trailing_space_size)
    turtle_object.pendown()


def if_10_in_a_row(dot_count):
    return (dot_count > 0) and (dot_count % 10 == 0)


# Load turtle object
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()

# Screen options
screen = Screen()

# Set colormode to 255 in order to feed rgb tuples to color
timmy.screen.colormode(255)

# Draw the dots
# Starting coordinates
y_coordinate = -225
x_coordinate = -225
timmy.penup()
timmy.goto(x_coordinate, y_coordinate)
timmy.pendown()

for dot_number in range(100):
    if if_10_in_a_row(dot_number):
        y_coordinate += 50
        timmy.penup()
        timmy.goto(x_coordinate, y_coordinate)
        timmy.pendown()
    # Reset the index so that the the colors in the list are used repeatedly once dot_number > len(color_rgb_list)
    correct_list_index = dot_number % len(color_rgb_list)
    timmy.color(color_rgb_list[correct_list_index])
    draw_dot_with_trailing_space(timmy, 20, 50)

screen.exitonclick()









