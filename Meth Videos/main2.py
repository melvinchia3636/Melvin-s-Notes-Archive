from manim import *


class GraphYeah(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 5),
            x_length=7,
            axis_config={"include_numbers": True},
        )
        axes.center()
        line_graph = axes.plot(
            lambda x: 2 * np.sin(x),
            x_range=[-5, 5, 0.01],
            color=BLUE,
        )

        self.play(Create(axes))
        self.wait(1)
        self.play(Create(line_graph))
