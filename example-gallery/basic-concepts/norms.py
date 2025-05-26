from manim import *



class Norms(Scene):
    def construct(self):
        dot_O = Dot(ORIGIN).set_color(GREEN)
        self.play(Write(dot_O))
        self.wait()

        numberplane = NumberPlane()
        self.play(Write(numberplane))
        self.wait()

        label_O = Tex(r"O (0, 0)").next_to(dot_O, DOWN).set_color(GREEN)
        self.play(Write(label_O))
        self.wait()

        arrow = Arrow(ORIGIN, [4, 3, 0], buff=0).set_color(GREEN)
        self.play(Write(arrow))
        self.wait()
        
        dot_A = Dot([4, 3, 0]).set_color(GREEN)
        self.play(Write(dot_A))
        self.wait()
        label_A = Tex(r"A (4, 3)").next_to(dot_A, UP).set_color(GREEN)
        self.play(Write(label_A))
        self.wait()
        
        dot_H = Dot([4, 0, 0]).set_color(RED)
        dashed_line_AH = DashedLine(
            dot_A.get_center(),
            dot_H.get_center()
        ).set_color(RED)
        line_OH = Line(dot_O.get_center(), dot_H.get_center()).set_color(RED)
        H_lines = [dashed_line_AH, line_OH]
        self.play(*[Write(l) for l in H_lines])
        self.wait()
        self.play(Write(dot_H))
        self.wait()
        label_H = Tex(r"H (4, 0)").next_to(dot_H, DOWN).set_color(RED)
        self.play(Write(label_H))
        self.wait()
        horiz_brace = Brace(line_OH).set_color(RED)
        horiz_text = horiz_brace.get_tex("OH = x_H - x_O").set_color(RED)
        self.play(
            ReplacementTransform(label_H, horiz_brace),
            Write(horiz_text)
        )
        self.wait()

        
        dot_K = Dot([0, 3, 0]).set_color(RED)
        dashed_line_AK = DashedLine(
            dot_A.get_center(),
            dot_K.get_center()
        ).set_color(RED)
        line_OK = Line(dot_O.get_center(), dot_K.get_center()).set_color(RED)
        K_lines = [dashed_line_AK, line_OK]
        self.play(*[Write(l) for l in K_lines])
        self.wait()
        horiz_text2 = horiz_brace.get_tex("OH = 4 - 0").set_color(RED)
        self.play(
            Write(dot_K),
            ReplacementTransform(horiz_text, horiz_text2)
        )
        self.wait()
        label_K = Tex(r"K (0, 3)").next_to(dot_K, LEFT).set_color(RED)
        self.play(Write(label_K))
        self.wait()
        vert_brace = Brace(
            line_OK,
            direction=line_OK.copy().rotate(PI / 2).get_unit_vector()
        ).set_color(RED)
        vert_text = vert_brace.get_tex("OK = y_K - y_O").set_color(RED)
        horiz_text3 = horiz_brace.get_tex("OH = 4").set_color(RED)
        self.play(
            ReplacementTransform(label_K, vert_brace),
            Write(vert_text),
            ReplacementTransform(horiz_text2, horiz_text3)
        )
        self.wait()

        vert_text2 = vert_brace.get_tex("OK = 3 - 0").set_color(RED)
        vert_text3 = vert_brace.get_tex("OK = 3").set_color(RED)
        vert_text4 = vert_brace.get_tex("3").set_color(RED)
        horiz_text4 = horiz_brace.get_tex("4").set_color(RED)
        self.play(
            ReplacementTransform(vert_text, vert_text2),
            ReplacementTransform(horiz_text3, horiz_text4)
        )
        self.play(ReplacementTransform(vert_text2, vert_text3))
        self.play(ReplacementTransform(vert_text3, vert_text4))
        self.wait()
        
        norm_brace = Brace(
            arrow,
            direction=arrow.copy().rotate(PI / 2).get_unit_vector()
        ).set_color(GREEN)
        norm_text = norm_brace.get_tex(
            "OA^2 = OH^2 + OK^2"
        ).set_color(GREEN)
        self.play(
            Write(norm_brace),
            Write(norm_text)
        )
        self.wait()
        
        dot_L = Dot([2, 1, 0]) # Below the vector to write the calculations
        norm_text2 = norm_brace.get_tex("OA^2 = 4^2 + 3^2").set_color(GREEN)
        self.play(
            ReplacementTransform(norm_text, norm_text2.next_to(dot_L, RIGHT))
        )
        norm_text3 = norm_brace.get_tex("OA^2 = 5^2").set_color(GREEN)
        self.play(
            ReplacementTransform(norm_text2, norm_text3)
        )
        self.wait()
        norm_text4 = norm_brace.get_tex("5").set_color(GREEN)
        self.play(
            ReplacementTransform(norm_text3, norm_text4)
        )
        self.wait()
        
            
        
        
    
