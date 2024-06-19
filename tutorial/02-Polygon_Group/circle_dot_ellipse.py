import numpy as np
from manim import *


class circle_dot_ellipse(Scene):
    def construct(self):
        cir_1 = Circle(radius=2, arc_center=np.array([2, 2, 0]), fill_color=YELLOW, stroke_color=BLUE, stroke_width=2,
                       fill_opacity=0.5)
        self.add(cir_1)
        self.play(cir_1.animate.move_to(LEFT * 2))
        dot_1 = Dot(stroke_width=5, point=RIGHT * 2 + UP * 2, color=RED, radius=2)
        self.play(FadeIn(dot_1))
        ellipse = Ellipse(height=5, width=10, fill_color=YELLOW, arc_center=np.array([2, -1, 0]), radius=3,
                          fill_opacity=0.5)
        self.play(FadeIn(ellipse))
