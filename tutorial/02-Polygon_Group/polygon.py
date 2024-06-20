from manim import *


class PolygonScene(Scene):
    def construct(self):
        p1 = np.array([0, 0, 0])
        p2 = np.array([1, 0, 0])
        p3 = np.array([0, 1, 0])
        triangle = Polygon(p1, p2, p3).set_fill(opacity=0.8, color=ORANGE)
        self.play(Write(triangle))
        p4 = np.array([2, 1.2, 0])
        p5 = np.array([3, 0, 0])
        p6 = np.array([-3, 1, 0])
        triangle2 = Polygon(p4, p5, p6).set_stroke(color=BLUE, width=2).round_corners(0.2)
        self.play(Write(triangle2))
        Reghep = RegularPolygon(7)
        self.play(Write(Reghep))
        Hexagon = RegularPolygon(6)
        self.play(Write(Hexagon))
        Regtri = Triangle()
        self.play(Write(Regtri))

