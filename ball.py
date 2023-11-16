import turtle
import random


class Ball:
    def __init__(self, size, x, y, i=0):
        self.size = size
        self.x = x
        self.y = y
        self.i = i
        self.xpos, self.ypos, self.ball_color = [], [], []
        self.vx, self.vy, self.color_list = [], [], []

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color[self.i])
        turtle.fillcolor(self.ball_color[self.i])
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self, canvas_width, canvas_height, ball_radius):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[self.i] += self.vx[self.i]
        self.ypos[self.i] += self.vy[self.i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[self.i] + self.vx[self.i]) > (canvas_width - ball_radius):
            self.vx[self.i] = -self.vx[self.i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[self.i] + self.vy[self.i]) > (canvas_height - ball_radius):
            self.vy[self.i] = -self.vy[self.i]

    def initilizing(self, canvas_width, canvas_height, ball_radius, num_balls):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(num_balls):
            self.xpos.append(random.randint(-1 * canvas_width + ball_radius, canvas_width - ball_radius))
            self.ypos.append(random.randint(-1 * canvas_height + ball_radius, canvas_height - ball_radius))
            self.vx.append(random.randint(1, 0.01 * canvas_width))
            self.vy.append(random.randint(1, 0.01 * canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
