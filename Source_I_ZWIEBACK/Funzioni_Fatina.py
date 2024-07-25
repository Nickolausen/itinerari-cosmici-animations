from manim import *

class Funzioni(Scene):
    def construct(self):
        eq_finale = MathTex(r"d_{OF}(t) = \left( L + v_ft\right)\left[ 1 - \frac{v_O}{v_F}\ln\left(\frac{L + v_Ft}{L}\right)\right]")
        eq_finale.scale(.7).to_corner(UR)

        func_1 = lambda x: (1 + x) * (1 - np.log(1 + .5 * x))
        func_2 = lambda x: (1 + x) * (1 - np.log(1 + .2 * x))
        func_3 = lambda x: (1 + x) * (1 - .6 * np.log(1 + .2 * x))

        ax = Axes(
            x_range=[-1, 25, 2],
            y_range=[-1, 4],
            axis_config={
                "tip_shape": StealthTip
            }
        )

        axes_label = ax.get_axis_labels(
            Tex("$anni$").scale(0.7), Tex("$d_{OF}(t)$").scale(0.7)
        )
        axes_label[0].shift(DOWN * .7)

        f1 = ax.plot(func_1, x_range=[-1, 4.5]).set_color(YELLOW)
        intersection1_dot = Dot(point = ax.c2p(3.4, 0)).set_color(YELLOW)
        intersection1_label = Tex(r"$8,5 \times 10^{36}$").next_to(intersection1_dot, UR, .1).scale(.5).shift(LEFT * .6).set_color(YELLOW)

        f2 = ax.plot(func_2, x_range=[-1, 9.9]).set_color(GREEN)
        intersection2_dot = Dot(point = ax.c2p(8.6, 0)).set_color(GREEN)
        intersection2_label = Tex(r"$6 \times 10^{427}$").next_to(intersection2_dot, UR, .1).scale(.5).shift(LEFT * .6).set_color(GREEN)

        f3 = ax.plot(func_3, x_range=[-1, 23.3]).set_color(BLUE)
        intersection3_dot = Dot(point = ax.c2p(21.5, 0)).set_color(BLUE)
        intersection3_label = Tex(r"$3 \times 10^{434284}$").next_to(intersection3_dot, UR, .1).scale(.5).shift(LEFT * .8).set_color(BLUE)

        labels = VGroup(intersection1_label, intersection2_label, intersection3_label)
        functions = VGroup(f1, f2, f3)
        dots = VGroup(intersection1_dot, intersection2_dot, intersection3_dot)

        self.play(AnimationGroup(Create(ax), Write(axes_label), Write(eq_finale), lag_ratio=.8), run_time=3)
        for idx, el in enumerate(functions):
            self.play(Create(functions[idx], rate_func=rate_functions.ease_in_expo, run_time=3))
            self.play(AnimationGroup(GrowFromCenter(dots[idx]), Write(labels[idx])), lag_ratio=.8)