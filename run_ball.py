import turtle
import ball


class Simulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls

    def display(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        ball_radius = 0.05 * canvas_width
        turtle.colormode(255)
        all_ball = ball.Ball(canvas_width, canvas_height, ball_radius, num_balls)
        all_ball.create_balls()
        while True:
            turtle.clear()
            for i in range(num_balls):
                all_ball.draw_circle(i)
                all_ball.move_circle(i)
            turtle.update()
        turtle.done()


num_balls = int(input("Number of balls to simulate: "))
Simulator(num_balls).display()