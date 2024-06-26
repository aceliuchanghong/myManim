import numpy as np
from manim import *


class FunctionScene(Scene):

    def construct(self):
        func = ParametricFunction(
            lambda t: np.array([
                2 * np.sin(3 * t) * np.cos(t),
                2 * np.sin(3 * t) * np.sin(t),
                0,
            ]),
            t_range=[0, 2 * PI, 0.01]
        ).set_color(RED).shift(UP * -1)
        self.play(Create(func.scale(3)))
        func2 = FunctionGraph(
            lambda x: x ** 2,
            x_range=[-4, 4],
            color=GREEN,
        )
        self.play(Create(func2))
