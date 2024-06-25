from manim import *


class image_scene(Scene):
    def construct(self):
        mob = ImageMobject(
            filename_or_array='../../using_files/img/20.png',
            invert=True,
        )
        mob.height = 3
        self.play(FadeIn(mob))
