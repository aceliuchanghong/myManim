from manim import *


class arc(Scene):
    def construct(self):
        arc_1 = Arc(angle=TAU / 3).add_tip()
        self.play(FadeIn(arc_1))
        self.wait()
        self.play(arc_1.animate.shift(LEFT * 1))
        self.wait()
        arc_1.add_tip(at_start=True)
        self.play(FadeIn(arc_1))
        cir_1 = Circle(radius=0.5)
        self.play(FadeIn(cir_1))
        self.wait()
        """
        alpha 参数用于指定切线相对于圆的位置。具体来说，alpha 是一个介于 0 和 1 之间的值，表示切线在圆周上的位置。
        当 alpha=0 时，切线在圆的起点（通常是右侧）。
        当 alpha=0.5 时，切线在圆的顶部。
        当 alpha=1 时，切线在圆的终点（通常是左侧）。
        """
        line = TangentLine(cir_1, alpha=0.2, length=6)
        self.play(FadeIn(line))
        arc_2 = Arc(arc_center=3 * LEFT, radius=2, stroke_width=4, start_angle=0 * DEGREES, angle=120 * DEGREES,
                    color=RED)
        self.play(FadeIn(arc_2))
