from manim import *



class BraceAnnotation(Scene):
    def construct(self):
        #self.camera.background_color = #
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.play(
            Write(line),
            Write(dot),
            Write(dot2),
            Write(b1),
            Write(b2),
            Write(b1text),
            Write(b2text)
        )
        self.wait()
        
