from manim import *

class Epicicli(Scene):
    def construct(self):
        bigger_circle = Circle(2.5)
        middle_line = Line(UP, DOWN).scale(3).shift(UP * .65)

        upper_circle = Circle(.7)
        upper_circle.shift(UP * 2.5)
        upper_upper_circle = Circle(.4)
        upper_upper_circle.shift(UP * 2.5 + UP * .7)

        middle_circle = Circle(.3)
        middle_circle.shift(UP * .5)

        P = always_redraw(lambda: Dot(radius=.08))
        self.add(bigger_circle, middle_line, upper_circle, upper_upper_circle, middle_circle)

        self.play(
            MoveAlongPath(P, middle_circle), 
            Rotate(
                upper_circle, 
                angle=2*PI, 
                about_point=[P.get_x(), P.get_y(), P.get_z()]), 
            run_time=5)

        