import numpy as np
from manim import *


class color(Scene):
    def construct(self):
        hex_color_1 = '#00FFEE'
        c1 = Circle(radius=2, fill_color=hex_color_1, fill_opacity=0.2)
        self.play(Write(c1))
        hex_color_2 = '#FF0000'
        c2 = Circle(radius=2, fill_color=hex_color_2, fill_opacity=0.2)
        # 使用 Transform 实现颜色的动画变化
        self.play(Transform(c1, c2))
        rgb_color_1 = np.array([0.4, 0.8, 1.0])

        print(hex_to_rgb(hex_color_1))
        print(rgb_to_hex(rgb_color_1))
        # rgb<==>int_rgb   ==>*255  <==/255
        print(rgb_to_color(hex_color_1))
