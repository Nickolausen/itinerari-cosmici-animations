from manim import *

class RandomHistogram2(Scene):
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

        function = chart.plot(lambda x: f(x + .5))
        function.set_color(ORANGE).set_stroke(width=8)

        integral = chart.get_area(graph=function)
        integral.set_fill(GREEN, .7)

        chart.remove(chart.bars)

        self.add(chart, function, integral)
        self.play(
            function.animate.shift(UP * 1.3),
            chart.animate.shift(UP * 1.3),
            integral.animate.shift(UP * 1.3))
        
        function_analytic = MathTex(r"f(x) = \frac{1}{2}\left(2x-1\right)\left(x-2\right)\left(x-3\right)\left(x-4\right)\left(x-5\right)+5",
                                    substrings_to_isolate=["f(x)"])
        function_analytic.set_color_by_tex("f(x)", ORANGE)

        function_analytic.next_to(chart, DOWN)
        
        integral_formula = MathTex("\int_{0}^{4} f(x) \,dx").next_to(function_analytic, DOWN)
        integral_formula.set_color(GREEN)
        
        integral_result = MathTex(r"= 18.4 \approx 20").next_to(integral_formula, RIGHT)
        whole_integral = VGroup(integral_formula, integral_result)
        whole_integral.next_to(function_analytic, DOWN)
        
        self.play(Write(function_analytic))
        self.wait(3)
        self.play(Write(integral_formula))
        self.wait()
        self.play(Write(integral_result))