from manim import *



class MoreMatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(
            MathTex("a"),
            MathTex("b"),
            MathTex("c")
        ).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait()
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
