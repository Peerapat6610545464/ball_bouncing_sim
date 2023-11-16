import turtle
from ball import Ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(10)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
ball = Ball(ball_radius)
ball.initilizing(canvas_width, canvas_height, ball_radius, num_balls)
while (True):
    turtle.clear()
    for i in range(num_balls):
        ball.i = i
        ball.draw_circle()
        ball.move_circle(canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
