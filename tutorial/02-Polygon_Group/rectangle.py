from manim import *


class rectangle(Scene):
    def construct(self):
        rectangle = Rectangle(
            color='#66CCFF', height=5, width=3, stroke_width=20, stroke_opacity=1, stroke_color=GREEN_B
            , sheen_factor=0.2, sheen_direction=UR
        ).round_corners(0.2)
        self.play(Write(rectangle))
        square = Square(side_length=2.5, fill_color=PURPLE_B, fill_opacity=1)
        self.play(Write(square))
        roundedrec = RoundedRectangle(corner_radius=-0.5, width=3, height=1)
        self.play(Write(roundedrec))
