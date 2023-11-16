import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls, xpos=None,
                 ypos=None, vx=None, vy=None, ball_color=None):
        if xpos is None:
            xpos = []
        if ypos is None:
            ypos = []
        if vx is None:
            vx = []
        if vy is None:
            vy = []
        if ball_color is None:
            ball_color = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.ball_color = ball_color

    def draw_circle(self, i):
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i], self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def create_balls(self):
        for _ in range(self.num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + self.ball_radius,
                                            self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(-1 * self.canvas_height + self.ball_radius,
                                            self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.canvas_height))
            self.ball_color.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def move_circle(self, i):
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]
