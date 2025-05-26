from manim import *


class BooleanOperations(Scene):
    def construct(self):
        setA = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        labelA = Tex(r"A").next_to(setA, DOWN).set_color(color=BLUE)
        
        setB = setA.copy().set_color(color=RED).move_to(RIGHT)
        labelB = Tex(r"B").next_to(setB, DOWN).set_color(color=RED)
        
        diff_text = Tex(
            r"Différence"
        ).next_to(setA, UP * 2.5)
        ellipse_group = Group(
            diff_text, setA, setB
        ).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))
        
        d1 = Difference(setA, setB, color=BLUE, fill_opacity=0.5)
        self.play(d1.animate.scale(0.4).move_to(RIGHT * 3.5 + UP * 1.5))
        d1_text = Tex(
            r"\(A\backslash B = A\cap B^{c}\)"
        ).next_to(d1, UP).set_color(color=BLUE)
        self.play(
            Write(d1_text)
        )
        
        d2 = Difference(setB, setA, color=RED, fill_opacity=0.5)
        d2_text = Tex(
            r"\(B\backslash A = B\cap A^{c}\)"
        ).next_to(d2, UP).set_color(color=RED)
        self.play(
            d2.animate.scale(0.4).next_to(d1, DOWN, buff=d2_text.height * 3)
        )
        d2_text.next_to(d2, DOWN).set_color(color=RED)
        self.play(Write(d2_text))

        
        
        
