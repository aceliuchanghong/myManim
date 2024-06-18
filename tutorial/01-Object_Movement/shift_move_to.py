from manim import *


class myTure01(Scene):
    def construct(self):
        mob = Circle(fill_opacity=1)
        self.add(mob)
        self.play(mob.animate.shift(LEFT * 5))
        self.wait(1)
        self.play(mob.animate.shift(UP * 2 + RIGHT * 3))
        self.wait(1)
        self.play(mob.animate.move_to(point_or_mobject=np.array([1, 1, 1]), aligned_edge=LEFT))
        self.wait(1)
