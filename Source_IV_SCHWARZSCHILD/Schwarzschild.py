from manim import *

class MegaFormula(Scene):
    def construct(self):
        tex_string = r"""
            ds^2 = \left( 1 - \frac{\alpha}{\sqrt[3]{r^3 + a^3}}\right)dt^2 - \frac{d\left(\sqrt[3]{r^3 + a^3}\right)^2}{1-\frac{\alpha}{\sqrt[3]{r^3 + a^3}}} - \sqrt[3]{(r^3 + a^3)^2}(d\theta^2 + \sin^2\theta d \phi^2)
        """

        title = Title("Soluzione esatta di Schwarzschild all'equazione di campo di Einstein").scale(.8)
        formula = MathTex(tex_string).scale(.8)

        self.play(Write(title))
        self.wait()
        self.play(Write(formula), run_time=4)
        self.play(Circumscribe(formula))