from manim import *


class CodeFromString(Scene):
    def construct(self):
        code_input = '''from manim import *


class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
'''

        rendered_code = Code(
            code=code_input,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace"
        )
        
        self.play(Write(rendered_code))
        self.wait()
