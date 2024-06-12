from manim import *


class Try(Scene):
    """
    manim main.py
    manim main.py -p
    """
    def construct(self):
        c = Circle(fill_opacity=1)
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(c, s))
        self.wait()
        self.play(FadeOut(s))
        self.wait()
