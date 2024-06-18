from manim import *


class scale_rotate(Scene):
    def construct(self):
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(Write(s))
        self.wait()
        self.play(s.animate.scale(2))
        self.wait()
        self.play(s.animate.scale(0.5, about_edge=UP))
        self.wait()
        self.play(s.animate.scale(0.5, about_point=np.array([-2, -2, 0])))
        self.wait()
        self.play(s.animate.rotate(90 * DEGREES))
        self.wait()
        self.play(s.animate.rotate(360 * DEGREES, axis=IN, about_point=ORIGIN))
        self.wait()
