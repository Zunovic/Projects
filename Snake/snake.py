from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.heading = self.segments[0]


    def create_snake(self):
        #Snake Objekte werden erstellt und nebeneinander platziert
        for pos in START_POS:
            self.add_segment(pos)


    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(pos)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.heading = self.segments[0]

    def move(self):
        # Snake bleibt verbunden und die einzelnen Segmente nehmen den Platz vom vorgänger ein
        for piece_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[piece_num - 1].xcor()
            new_y = self.segments[piece_num - 1].ycor()
            self.segments[piece_num].goto(new_x, new_y)
        self.heading.forward(MOVE_DIST)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.heading.heading() != DOWN:
            self.heading.setheading(UP)


    def down(self):
       if self.heading.heading() != UP:
           self.heading.setheading(DOWN)


    def left(self):
       if self.heading.heading() != RIGHT:
           self.heading.setheading(LEFT)


    def right(self):
       if self.heading.heading() != LEFT:
           self.heading.setheading(RIGHT)
