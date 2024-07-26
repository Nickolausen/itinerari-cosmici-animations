from manim import *
from Sorgente_BT4 import main_text, citation_text

class Battute(Scene):
    def construct(self):
        display = Tex(main_text).scale(.8)
        citation = Tex(citation_text).next_to(display, DOWN).scale(.6)

        whole = VGroup(display, citation).move_to(ORIGIN)
        self.play(Write(display), run_time=5)
        self.play(Write(citation))