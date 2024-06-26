from manim import *


class axes_scene(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        ax.add_coordinates([-1, 2])
        ax.get_axis_labels()
        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.add(ax, graph)
        self.play(FadeIn(graph))
        ax2 = Axes(axis_config={'tip_shape': StealthTip})
        self.add(ax2)
        self.play(ax2.animate.shift(RIGHT))
