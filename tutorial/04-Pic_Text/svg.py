from manim import *


class svg_scene(Scene):
    def construct(self):
        mob = SVGMobject(
            file_name='../../using_files/svg/20.svg',
            color=BLUE,
            stroke_width=0.5
        )
        self.play(Write(mob))
        self.play(Uncreate(mob))
