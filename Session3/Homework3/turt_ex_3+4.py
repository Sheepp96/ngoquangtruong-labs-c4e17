from turtle import *


def draw_square(x, y):

    for i in range(4):
        color(y)
        forward(x)
        lt(90)

# a = draw_square(90, 'blue')

for j in range(30):
    draw_square(j * 5, 'red')
    lt(17)
    penup()
    forward(j * 2)
    pendown()

mainloop()
