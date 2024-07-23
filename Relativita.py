from manim import *

class Relativita(Scene):
    def construct(self):
        title = Title("Equazioni di campo di Einstein")
        formula = MathTex(r"\underbrace{R_{\mu v} - \frac{1}{2}Rg_{\mu v}}_{\text{Geometria dello spazio}} = \underbrace{8\pi G T_{\mu v}}_{\text{Massa, Energia}}").scale(1.5)

        self.play(Write(title))
        self.play(Write(formula), run_time=4)
        self.wait()
        self.play(Circumscribe(formula))