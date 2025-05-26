from manim import *



class Distance(Scene):
    def construct(self):
        #self.camera.background_color = 
        dot_A = Dot([-2, -1, 0])
        label_A = Tex("A").next_to(dot_A, LEFT)
                
        dot_B = Dot([2, 1, 0])
        label_B = Tex("B").next_to(dot_B, UP)

        dot_C = Dot([2, -1, 0])
        label_C = Tex("C").next_to(dot_C, DR)
        
        line_AB = Line(
            dot_A.get_center(),
            dot_B.get_center()
        ).set_color(GREEN)

        line_AC = DashedLine(
            dot_A.get_center(),
            dot_C.get_center()
        ).set_color(RED)

        line_CB = DashedLine(
            dot_C.get_center(),
            dot_B.get_center()
        ).set_color(RED)
        
        v1 = Brace(
            line_CB,
            direction=line_CB.copy().rotate(-PI / 2).get_unit_vector()
        )
        v1text = v1.get_tex("y_B - y_C = y_B - y_A")
    
        h1 = Brace(line_AC)
        h1text = h1.get_tex("x_C - x_A = x_B - x_A")
        
        b2 = Brace(
            line_AB,
            direction=line_AB.copy().rotate(PI / 2).get_unit_vector()
        )
        b2text = b2.get_tex(
            "AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}"
        ).scale(0.75)

        self.play(
            *[Write(o) for o in [dot_A, label_A]]
        )
        self.wait()

        self.play(
            *[Write(o) for o in [dot_B, label_B]]
        )
        self.wait()

        self.play(Write(line_AB))
        self.wait()

        self.play(
            Write(line_AC),
            Write(dot_C),
            Write(label_C)
        )
        self.wait()
        
        self.play(
            Write(h1),
            Write(h1text),
        )
        self.wait()

        self.play(
            Write(line_CB)
        )
        self.wait()

        self.play(
            Write(v1),
            Write(v1text)
        )
        self.wait()

        self.play(
            Write(b2),
            Write(b2text)
        )
        self.wait()
        
