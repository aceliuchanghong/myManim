from manim import *


class flip_stretch(Scene):
    def construct(self):
        s = Square(color=YELLOW, fill_opacity=1)
        s2 = Square(color=RED, fill_opacity=1)
        self.play(Write(s))
        self.wait()
        self.play(s.animate.to_corner(UL, buff=0))
        self.wait()
        for i in range(1, 4):
            self.play(s.animate.to_corner(UL, buff=i * 0.5))
            self.wait()
        self.add(s2)
        self.play(s2.animate.to_corner(DL, buff=0))
        self.wait()
        for i in range(0, 3):
            self.play(s2.animate.to_corner(DL, buff=i * 0.5))
            self.wait()
        self.play(s.animate.align_to(mobject_or_point=s2, direction=RIGHT))
        self.wait()
