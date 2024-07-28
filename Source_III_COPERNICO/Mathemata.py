from manim import *

class Mathemata(Scene):
    def construct(self):
        scritta = Tex('“Mathemata mathematicis scribuntur”').scale(1.2)
        self.play(Write(scritta))