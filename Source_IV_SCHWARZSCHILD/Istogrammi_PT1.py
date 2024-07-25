from manim import *

class RandomHistogram(Scene):
    def construct(self):
        chart = BarChart(
            values=[0, 0, 0, 0],
            y_range=[0, 18, 2],
            bar_colors=[YELLOW, GREEN, MAROON, TEAL]
        )
        
        def f(x):
            # if (x >= 0 and x <= 1): return 10 * x
            # if (x > 1 and x <= 2): return (30 * x) - 20
            # if (x > 2 and x <= 3): return (-20 * x) + 80
            # if (x > 3 and x <= 4): return 20
            # if (x > 4 and x <= 5): return 10 * x - 20
            # else: return 30 
            return .5 * (2*x - 1)*(x - 2)*(x - 3)*(x - 4)*(x - 5) + 5

        final_values = [17, 3, 4, 7, .5]

        self.play(Create(chart))
        self.wait()

        self.play(chart.animate.change_bar_values(final_values), run_time=5)
        self.wait()
        
        dots = VGroup()
        total = 0

        dots.add(Dot(point=chart.get_origin(), radius=.1))
        total += 1
        for bar in chart.bars:
            total += 1
            dot = Dot(point=bar.get_top(), radius=.1)
            dots.add(dot)

        links = VGroup() 
        idx = 0
        for dot in dots:
            if (idx + 1 < total):
                link = Line(start=dot, end=dots[idx + 1])
                links.add(link)
                idx += 1
        
        function = chart.plot(lambda x: f(x + .5))
        function.set_color(ORANGE).set_stroke(width=8)

        integral = chart.get_area(graph=function)
        integral.set_fill(TEAL, .7)

        self.play(AnimationGroup(*[FadeIn(dot) for dot in dots], lag_ratio=.7))
        self.wait()
        self.play(AnimationGroup(*[Create(link) for link in links], lag_ratio=.7))
        self.play(
            FadeOut(chart.bars, links, dots), 
            FadeIn(function, integral), 
            run_time=4)