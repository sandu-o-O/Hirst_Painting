#https://www.udemy.com/course/100-days-of-code/learn/lecture/20264902#overview
'''import colorgram

rgb_colors = []

colors = colorgram.extract('art.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)'''
import turtle as turtle_module
import random

color_list = [(239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50), (212, 127, 164), (34, 194, 117), (139, 183, 18), (189, 18, 39), (108, 105, 194), (232, 55, 45), (244, 147, 183), (113, 191, 149), (191, 46, 66), (19, 187, 206), (45, 52, 105), (136, 221, 240), (146, 229, 169), (202, 210, 7), (22, 151, 116), (233, 174, 159), (31, 43, 76), (112, 42, 40), (181, 178, 220), (80, 34, 37)]

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed(0)
tim.setpos(-200, -200)


def draw_a_horizontal_line(num_of_dots):
    for _ in range(num_of_dots):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


y = -200
for _ in range(10):
    tim.penup()
    tim.setpos(-200, y)
    draw_a_horizontal_line(10)
    y += 50


screen = turtle_module.Screen()
screen.exitonclick()