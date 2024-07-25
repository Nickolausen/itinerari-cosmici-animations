from manim import *

class FormuleZwieback_1(Scene):
    def construct(self):
        armonica1 = MathTex(r"\Theta(1) = \frac{v_o}{L + v_f}")
        armonica2 = MathTex(r"\Theta(2) = \frac{v_o}{L + v_f} + \frac{v_o}{L + 2v_f}")
        armonica3 = MathTex(r"\Theta(n) = \frac{v_o}{L + v_f} + \frac{v_o}{L + 2v_f} + \dots + \frac{v_o}{L + nv_f}")
        armonica4 = MathTex(r"\Theta(n) \geq \frac{v_o}{L + v_f} + \frac{v_o}{2L + 2v_f} + \frac{v_o}{3 L + 3 v_f} + \dots + \frac{v_o}{n L + n v_f}")
        armonica5 = MathTex(r"\Theta(n) \geq \frac{v_o}{L + v_f} \underbrace{\left(1 + \frac{1}{2} +  \dots + \frac{1}{n} \right)}_{\text{Serie armonica! } \to \infty}", 
            substrings_to_isolate=[r"\underbrace{\left(1 + \frac{1}{2} +  \dots + \frac{1}{n} \right)}_{\text{Serie armonica! } \to \infty}"])
        
        armonica_group = VGroup(armonica1, armonica2, armonica3, armonica4, armonica5)
        armonica_group.scale(.8).arrange_in_grid(rows=5, cell_alignment=LEFT)
        
        for formula in armonica_group:
            self.play(Write(formula), run_time=2.5)
            self.wait()

        self.play(armonica5.animate.set_color_by_tex(r"\underbrace{\left(1 + \frac{1}{2} +  \dots + \frac{1}{n} \right)}_{\text{Serie armonica! } \to \infty}", YELLOW)) 