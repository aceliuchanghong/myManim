import numpy as np
from manim import *


class plane_scene(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=5,
            y_length=2,
            axis_config={
                "stroke_width": 2,
                "stroke_color": YELLOW,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "font_size": 24,
            }
        ).move_to(LEFT * 3)

        number_plane_scaled_y = NumberPlane(
            x_range=(-4, 11, 1),
            x_length=5,
            y_length=4,
        ).move_to(RIGHT * 3)

        self.add(grid)
        self.add(number_plane_scaled_y)
        self.play(FadeIn(grid))
        self.play(FadeIn(number_plane_scaled_y))
        grid.apply_function(lambda x: x + UP * 2)
        self.play(FadeOut(grid))
        grid.prepare_for_nonlinear_transform()
        grid.apply_function(lambda y: y + np.array([
            np.sin(y[1]), np.sin(y[0]), 0
        ]))
        self.play(Write(grid))
        number_plane_scaled_y.add_coordinates()
        self.play(FadeOut(number_plane_scaled_y))
        number_plane_scaled_y.prepare_for_nonlinear_transform()
        number_plane_scaled_y.apply_complex_function(lambda z: np.exp(z))
        self.play(Write(number_plane_scaled_y))
