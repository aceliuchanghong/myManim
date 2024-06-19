from manim import *


class line_arrow(Scene):
    def construct(self):
        line_1 = Line()
        line_2 = Line(np.array([-2, -2, 0]), np.array([2, 3, 0]), buff=0.8)
        line_3 = Line(np.array([-2.5, -1.22, 0]), np.array([2.1, 1.3, 0]), buff=0.1, stroke_width=3)
        self.play(Write(line_1))
        self.play(Write(line_2))
        self.play(Write(line_3))
        self.wait()
        line_4 = DashedLine(np.array([-5, -2, 0]), np.array([2, 3, 0]), buff=1, stroke_color=BLUE, path_arc=2.16)
        self.play(Write(line_4))
        self.wait()

        line_5 = Line(np.array([2, -2, 0]), np.array([2, -3, 0]), buff=0.8)
        self.play(Write(line_5))
        self.wait()
        line_5.add_tip()
        self.wait()
        vec_1 = Arrow(np.array([-4, -2, 0]), np.array([2, 4, 0]), buff=0.8, tip_length=0.9)
        self.play(Write(vec_1))
        self.wait()
        vec_2 = Vector(LEFT * 3 + UP * 5)
        self.play(vec_2.animate.scale(2))
        self.play(vec_2.animate.shift(RIGHT * 3))
        vec_3 = DoubleArrow(np.array([5.2, -2, 0]), np.array([2, -3, 0]), buff=2)
        self.play(vec_3.animate.shift(RIGHT * 3))
