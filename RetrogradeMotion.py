from manim import *

class Epicycle(Scene):
    def construct(self):
        center = Dot(radius=.15)
        inner_circle = Circle(radius=1.3).shift(UP * .3)
        outer_circle = Circle(radius=3.5).shift(DOWN * .3)

        outer_planet = Dot(radius=.10)
        inner_planet = Dot(radius=.05)
        
        line_slope = ValueTracker(0)

        def draw_line():
            output = Line(start=outer_planet.get_center(), end=inner_planet.get_center())
            line_slope.set_value(output.get_slope())
            return output

        line = always_redraw(lambda: draw_line())
        line_continue = always_redraw(lambda: Line(start=inner_planet.get_center()))
        
        self.add(center, inner_circle, outer_circle, outer_planet, inner_planet, line)
        for _ in range(0, 3):
            self.play(
                MoveAlongPath(outer_planet, outer_circle, run_time=4, rate_func=linear),
                MoveAlongPath(inner_planet, inner_circle, run_time=4, rate_func=linear))