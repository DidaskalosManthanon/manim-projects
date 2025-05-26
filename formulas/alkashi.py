from manim import *



class AlKashi(Scene):
    def construct(self):
        title = Title("Théorème d'Al Kashi (Pythagore généralisé)")
        self.play(Write(title))
        self.wait()
        numberplane = NumberPlane()
        self.play(
            Write(numberplane)
        )
        self.wait()
        dot_A = Dot([-5, -2, 0])
        label_A = Tex(r"A(-5, -2)").next_to(dot_A, DOWN)        
        dot_B = Dot([-2, -2, 0])
        line_AB = Line(dot_A.get_center(), dot_B.get_center()).set_color(RED)
        label_B = Tex(r"B(-2, -2)").next_to(dot_B, DOWN)


        radius = np.sqrt(16)
        initial_angle = PI / 2
        final_angle = 2 * PI
        dot_C = Dot(
            dot_B.get_center() + \
            radius * RIGHT * np.cos(initial_angle) + \
            radius * UP * np.sin(initial_angle)
        )
        label_C = Tex(
            r"\(C\left(-2, 2)\)"
        ).next_to(dot_C, RIGHT)

        line_BC = Line(dot_B.get_center(), dot_C.get_center())
        line_CA = Line(dot_C.get_center(), dot_A.get_center()).set_color(RED)

        init_objs = [
            dot_A, dot_B, dot_C,
            label_A, label_B, label_C,
            line_AB, line_BC, line_CA
        ]
        for o in init_objs:
            self.play(
                Write(o.set_color(RED)),
            )
            self.wait()
        
        # Create angle indicator
        angle_indicator = Angle(
            line_BC, Line(dot_B.get_center(), dot_A.get_center()),
            radius=0.5,
            color=YELLOW
            )

        pythagore = r"\overrightarrow{AC}^2 &= "
        pythagore += r"(\overrightarrow{AB} + \overrightarrow{BC})^2 ="
        pythagore += r"(\overrightarrow{BC} - \overrightarrow{AB})^2\\"
        pythagore += r"&= \overrightarrow{AB}^2 - "
        pythagore += r"2\overrightarrow{BA}\cdot\overrightarrow{BC} + "
        pythagore += r"\overrightarrow{BC}^2\\"
        pythagore += r"&= \overrightarrow{AB}^2 -2"
        pythagore += r"\cos\left(\overrightarrow{BC},\overrightarrow{BA}\right)"
        pythagore += r"+ \overrightarrow{BC}^2\\"
        formula = MathTex(
            pythagore,
            # tex_template=TexFontTemplates.french_cursive,
            font_size=42
        ).next_to(dot_C, DOWN)
        self.play(
            Write(formula),
            run_time=5
        )
        self.wait()
        
        trajectory_circle = Circle(radius=radius).set_color(BLUE_A)
        trajectory_circle.move_to(dot_B.get_center())
        self.play(Create(trajectory_circle))

        
        def update_label_C(mob):
            x, y, _ = dot_C.get_center()
            new_label = Tex(
                f"C({x:.2f}, {y:.2f})"
            ).next_to(dot_C, UP).set_color(RED)
            mob.become(new_label)

            
        def update_line_BC(mob):
            mob.put_start_and_end_on(dot_B.get_center(), dot_C.get_center())

            
        def update_line_CA(mob):
            mob.put_start_and_end_on(dot_C.get_center(), dot_A.get_center())

            
        def update_angle(mob):
            line1 = Line(dot_B.get_center(), dot_C.get_center())
            line2 = Line(dot_B.get_center(), dot_A.get_center())
            if not np.allclose(
                    line1.get_vector(),
                    line2.get_vector(),
                    atol=1e-2
            ):
                new_angle = Angle(
                    line1,
                    line2,
                    radius=0.5,
                    color=YELLOW
                )
                mob.become(new_angle)

            
        def update_formula(mob):
            mob.next_to(dot_C, DOWN)

            
        # Add updaters
        label_C.add_updater(update_label_C)
        line_BC.add_updater(update_line_BC)
        line_CA.add_updater(update_line_CA)
        angle_indicator.add_updater(update_angle)
        formula.add_updater(update_formula)

        self.play(
            Create(angle_indicator)
        )
        
        # Animate C's movement along the arc
        self.play(
            Rotate(dot_C, angle=final_angle, about_point=dot_B.get_center()),
            run_time=5,
            rate_func=smooth
        )

        # Remove updaters
        label_C.clear_updaters()
        line_BC.clear_updaters()
        line_CA.clear_updaters()
        angle_indicator.clear_updaters()

        final_formula = MathTex(
            r"\overrightarrow{AC}^2 =",
            r"\overrightarrow{AB^2} + ",
            r"\overrightarrow{BC^2} - ",
            r"2\cos\left(\overrightarrow{BC}, \overrightarrow{BA}\right)",
            font_size=48
        ).set_color(GREEN)
        self.play(
            ReplacementTransform(formula, final_formula.next_to(dot_C, DR))
        )
        self.wait()

        vect_BC = Arrow(
            dot_B.get_center(),
            dot_C.get_center()
        )
        vect_BA = Arrow(
            dot_B.get_center(),
            dot_A.get_center()
        )
        vect_AC = Arrow(
            dot_A.get_center(),
            dot_C.get_center()
        )
        vects = [vect_BC, vect_BA, vect_AC]
        
        box = SurroundingRectangle(final_formula)
        self.play(
            *[Write(v.set_color(GREEN)) for v in vects],
            Write(box)
        )
        self.wait()

        group_box = VGroup(final_formula, box)
        self.play(
            group_box.animate.shift(2 * 0.75 * DOWN)
        )
        self.wait()
