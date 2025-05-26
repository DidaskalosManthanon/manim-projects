from manim import *


class BooleanOperations(Scene):
    def construct(self):
        setA = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        labelA = Tex(r"A").set_color(color=BLUE).next_to(setA, DOWN)
        
        setB = setA.copy().set_color(color=RED).move_to(RIGHT)
        labelB = Tex(r"B").set_color(color=RED).next_to(setB, DOWN)
        
        union_title = Tex(
            r"Union "
        ).next_to(setA, UP * 3).set_color(color=ORANGE)
        ellipse_group = Group(
            union_title, setA, setB, labelA, labelB
        ).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))
                
        u = Union(setA, setB, color=ORANGE, fill_opacity=0.5)
        u_move = u.copy()
        
        union_text = Tex(r"\(A\cup B\)").set_color(color=ORANGE)
        union_move_txt = union_text.copy()
        union_title_2 = Tex(
            r"Union \(A\cup B\)"
        ).next_to(setA, UP * 3).set_color(color=ORANGE)
        
        self.play(
            u_move.animate.move_to(RIGHT * 3.75)
        )
        union_move_txt.next_to(u_move, DOWN)
        union_text.next_to(u, UP * 1.25)
        self.play(
            FadeIn(union_move_txt),
            ReplacementTransform(union_title, union_title_2)
        )
        self.wait()

