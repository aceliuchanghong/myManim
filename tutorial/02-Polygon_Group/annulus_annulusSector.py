from manim import *


class annulus_annulusSector(Scene):
    def construct(self):
        annulus_1 = Annulus(
            outer_radius=3, inner_radius=3, fill_color=RED, fill_opacity=0.7, stroke_width=10, stroke_color=YELLOW
        )
        self.add(annulus_1)
        self.play(Write(annulus_1))
        ann_sec = AnnularSector(
            inner_radius=3, outer_radius=2, start_angle=PI / 6, angle=PI / 3, fill_color=BLUE, fill_opacity=0.7,
            stroke_width=10, stroke_color=GOLD_B, arc_center=np.array([2, 2, 0])
        )
        self.play(Write(ann_sec))
        self.play(ann_sec.animate.shift(LEFT * 3))
