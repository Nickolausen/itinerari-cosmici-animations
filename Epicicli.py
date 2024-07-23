from manim import *

class Epicicli(Scene):
    def construct(self):
        bigger_circle = Circle(2.5)
        middle_line = Line(UP, DOWN).scale(3).shift(UP * .6)

        upper_circle = Circle(1.5)
        upper_circle.move_to(Intersection(bigger_circle, middle_line).get_center())

        self.add(bigger_circle, middle_line, upper_circle)