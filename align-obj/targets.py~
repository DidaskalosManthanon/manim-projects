from manim import *


class Targets(Scene):
    def construct(self):
        white_circ = [
            Circle(
                radius=3 - 3 * i / 11,
                color=WHITE
            ) for i in range(11)
        ]

        self.play(*[Write(o) for o in white_circ])
        self.wait()

        col_op = [
            (WHITE, 1), (WHITE, 1),
            (BLACK, 1), (BLACK, 1),
            (BLUE, 1), (BLUE, 1),
            (RED, 1), (RED, 1),
            (YELLOW, 1), (YELLOW, 1), (YELLOW, 1)
        ]
        
        def objects_to_fill(self, objects, col_op):
            self.play(
                *[
                    objects[i].animate.set_fill(
                    color=col_op[i][0],
                    opacity=col_op[i][1]) for i in range(len(objects))
                ]
            )
            self.wait()

        objects_to_fill(self, white_circ, col_op)

        # Original positions for circles
        circ_origin_pos = [c.get_center() for c in white_circ]

        directions = [RIGHT, UP, LEFT, DOWN]
        
        for dir in directions:
            self.play(
                *[c.animate.align_to(white_circ[0], dir) for c in white_circ]
            )
            self.wait()
            
            # Come back to original positions
            self.play(
                *[
                    c.animate.move_to(pos)
                    for c, pos in zip(white_circ, circ_origin_pos)
                ]
            )
            self.wait()
            

        
        squares = [
            Square(
                side_length=2 * ( 3 - 3 * i / 11),
                color=col_op[i][0],
            ) for i in range(11)
        ]
        
        change = [
            white_circ[i].become(squares[i]) for i in range(len(white_circ))
        ]

        self.play(*[Write(o) for o in change])
        self.wait()

        objects_to_fill(self, squares, col_op)

        # Original positions for squares
        sqr_origin_pos = [s.get_center() for s in squares]

        for dir in directions:
            self.play(
                *[s.animate.align_to(squares[-1], dir) for s in squares]
            )
            self.wait()

            # Come back to original positions
            self.play(
                *[
                    s.animate.move_to(pos)
                    for s, pos in zip(squares, sqr_origin_pos)
                ]
            )
            self.wait()
            

        
            
