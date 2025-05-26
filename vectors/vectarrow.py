from manim import *


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        self.play(
            Create(dot)
        )
        self.wait()
        
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        self.play(Write(arrow))
        self.wait()
        
        numberplane = NumberPlane()
        self.play(
            Create(numberplane)
        )
        self.wait()
        
        origin_text = Tex(r"(0, 0)").next_to(dot, DOWN)
        self.play(
            Write(origin_text)
        )
        self.wait()
        
        tip_text = Tex(r"(2, 2)").next_to(arrow.get_end(), RIGHT)
        self.play(
            Write(tip_text)
        )
        self.wait()
