from manim import *



class Animate(Scene):
    def construct(self):
        square = Square(color=RED).shift(LEFT * 2)
        circle = Circle(color=BLUE).shift(RIGHT * 2)

        self.play(Write(square), Write(circle))

        # moving objects
        self.play(
            square.animate.shift(UP * 0.5),
            circle.animate.shift(DOWN * 0.5)
        )

        # rotating and filling the square (opacity 80%)
        # scaling and filling the circle (opacity 80%)
        self.play(
            square.animate.rotate(PI / 2).set_fill(RED, 0.8),
            circle.animate.scale(2).set_fill(BLUE, 0.8)
        )

        # change color
        self.play(
            square.animate.set_color(GREEN),
            circle.animate.set_color(ORANGE)
        )

        self.play(FadeOut(square), FadeOut(circle))
        
