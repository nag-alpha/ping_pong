from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        current_y = self.ycor()
        if current_y >= 240:
            return
        self.goto(x=self.xcor(), y=current_y + 20)

    def move_down(self):
        current_y = self.ycor()
        if current_y <= -240:
            return
        self.goto(x=self.xcor(), y=current_y - 20)


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.color("white")
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def show_scores(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Ariel", 30, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Ariel", 30, "normal"))

    def update_score_left(self):
        self.l_score += 1

    def update_score_right(self):
        self.r_score += 1
