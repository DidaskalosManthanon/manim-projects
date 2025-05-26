from manim import *


class CodeFromFile(Scene):
    def construct(self):
        #animate_syntax = "../anim-syntax/animate_syntax.py"
        code_from_str = "./codefromstring.py"
        
        code_to_disp = Code(
            file_name=code_from_str,
            tab_width=4,
            line_spacing=0.3,
            font_size=18,
            background="rectangle",
            language="Python",
            font="Monospace"
        )

        self.play(
            Write(code_to_disp),
            run_time=5
        )
        self.wait(5)
