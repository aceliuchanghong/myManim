from manim import *


class vgroup(Scene):
    def construct(self):
        Reghep = RegularPolygon(7)
        self.play(Write(Reghep))
        Hexagon = RegularPolygon(6)
        self.play(Write(Hexagon))
        Regtri = Triangle()
        self.play(Write(Regtri))
        square = Square(side_length=2.5, fill_color=PURPLE_B, fill_opacity=0.11)
        self.play(Write(square))
        b = VGroup(Regtri, Reghep, Hexagon)
        b.add(square)
        self.play(b.animate.shift(LEFT * 3))
        b.remove(b[2])
        self.play(b.animate.shift(RIGHT * 3))
        self.play(b[1].animate.shift(RIGHT * 3))

