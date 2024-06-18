from manim import *


class Circle2Square(Scene):
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


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)
