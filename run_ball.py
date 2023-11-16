import turtle

import self as self

from ball import Ball


class Simulation:
    def __init__(self, num_ball, speed, size):
        self.num_ball = num_ball
        self.speed = speed
        self.size = size
        turtle.speed(self.speed)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

    def start(self):
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        ball_radius = 0.05 * canvas_width * (self.size + 1)
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


num_balls = int(input("Number of balls to simulate: "))
speed = int(input("set ball speed: "))
size_ = int(input("set ball size: "))
sim = Simulation(num_balls, speed, size_)
sim.start()
