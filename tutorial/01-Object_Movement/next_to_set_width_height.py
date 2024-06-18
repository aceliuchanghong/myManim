from manim import *


class next_to_set_width_hight(Scene):
    def construct(self):
        s1 = Circle(color=YELLOW, radius=0.5, fill_opacity=1)
        s2 = Square(side_length=0.5, color=RED, fill_opacity=1)
        self.add(s1)
        self.add(s2)
        self.play(FadeIn(s1))
        self.play(FadeIn(s2))
        self.play(s1.animate.shift(RIGHT * 5))
        self.wait()
        self.play(s1.animate.next_to(s2))
        self.wait()
        self.play(s1.animate.next_to(s2, UP))
        self.wait()
        self.play(s1.animate.next_to(mobject_or_point=s2, direction=DOWN, buff=1))
        self.wait()

        s3 = Circle(color=GRAY_B, radius=1, fill_opacity=0)
        s4 = Circle(color=GOLD_B, radius=1.5, fill_opacity=0)
        self.add(s3, s4)
        A = VGroup(s3, s4)
        B = VGroup(s1, s2)
        self.play(A.animate.next_to(B[1], DOWN, aligned_edge=LEFT))
        self.wait()

        img = ImageMobject('../../using_files/img/20.jpg')
        self.play(img.animate.scale(0.75))
        self.wait()
        img.set_width(1.5)
        self.wait()
        img.set_height(0.5)
        self.wait()
