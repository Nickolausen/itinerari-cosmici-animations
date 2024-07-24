from manim import *

class TensoreImpulsoEnergia(Scene):
    def construct(self):

        tex_string = r"""\begin{bmatrix}
            T_{00} & T_{01} & T_{02} & T_{03} \\
            T_{10} & T_{11} & T_{12} & T_{13} \\
            T_{20} & T_{21} & T_{22} & T_{23} \\
            T_{30} & T_{31} & T_{32} & T_{33}
            \end{bmatrix}"""

        title = Title("Tensore impulso energia")
        formula = MathTex(
            tex_string
        )

        self.play(Write(title))
        self.wait()
        self.play(Write(formula))
        self.play(Circumscribe(formula))