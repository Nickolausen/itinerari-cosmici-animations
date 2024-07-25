from manim import *

class FormuleZwieback_2(Scene):
    def construct(self):
        eq_finale = MathTex(r"y_{O}(t) = \left( L + v_ft\right) \frac{v_O}{v_F}\ln\left(\frac{L + v_Ft}{L}\right)")
        eq_finale_derivata = MathTex(r"y_{O}'(t) = \frac{v_{F}y_{O}(t)}{L + v_{F}t} + v_O")
        eq_finale_derivata.next_to(eq_finale, DOWN)
        formule = VGroup(eq_finale, eq_finale_derivata).move_to(ORIGIN)

        self.play(Write(eq_finale))
        self.wait()
        self.play(Write(eq_finale_derivata))