from manim import *


class text_scene(Scene):
    def construct(self):
        text = Text(
            text="愿起一剑杀万劫--siscon",
            height=0.5,
            stroke_width=0.1,
            stroke_color=PURPLE_B,
            color=YELLOW
        )
        text2 = Text(
            text="jiejiejie",
            height=0.2,
            stroke_width=0.22,
            stroke_color=BLUE,
            color=RED
        )
        self.play(Write(text))
        self.play(Write(text2))
        self.play(text2.animate.shift(UL * 3))
        self.play(text.animate.move_to(text2))

        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))
        self.play(Write(title))
        t1 = Text("1. Measuring").set_color(WHITE)
        t2 = Text("2. Clustering").set_color(WHITE)
        t3 = Text("3. Regression").set_color(WHITE)
        t4 = Text("4. Prediction").set_color(WHITE)
        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN, DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)
        self.play(Write(x))
