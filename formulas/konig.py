from manim import *



class Konig(Scene):
    def construct(self):
        title = Title("Formule de König")
        self.play(Write(title))
        self.wait()
        var = r"\mathbb{V}[X] &= "
        var += r"\mathbb{E}\left[\left(X - \mathbb{E}[X]\right)^2\right]\\&="
        var += r"\mathbb{E}\left[X^2-2X\mathbb{E}[X] + \mathbb{E}[X]^2\right]\\"
        var += r"&= \mathbb{E}[X^2] - 2\mathbb{E}[X]^2 + \mathbb{E}[X]^2\\"
        var += r"&= \mathbb{E}[X^2] - \mathbb{E}[X]^2"
        formula = MathTex(
            var,
            font_size=72
        )
        self.play(
            Write(formula),
            run_time=5
        )
        self.wait()
