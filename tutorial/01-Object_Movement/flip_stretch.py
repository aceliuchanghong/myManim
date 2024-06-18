from manim import *


class flip_stretch(Scene):
    def construct(self):
        mob = Circle(fill_opacity=0.5, color=BLUE)
        self.add(mob)
        self.play(FadeIn(mob))
        self.wait()
        self.play(mob.animate.flip())
        self.wait()
        self.play(mob.animate.shift(UP * 2 + LEFT * 2))
        self.wait()
        self.play(mob.animate.flip(axis=RIGHT))
        self.wait()
        self.play(mob.animate.flip(axis=RIGHT, about_point=ORIGIN))
        self.wait()
        self.play(mob.animate.stretch(factor=2, dim=1))
        self.wait()
        self.play(mob.animate.shift(UP * 0.5))
        self.wait()
        self.play(mob.animate.stretch(factor=2, dim=1, about_point=np.array([-2, -2, 0])))
        self.wait()
