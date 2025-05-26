from manim import *



class Modif(Scene):
    def construct(self):
        # create square and circle objects (and move them)
        square1 = Square(color=BLUE).shift(LEFT * 4)
        circle = Circle(color=GREEN).shift(UP * 2)
        square2 = Square(color=RED).shift(RIGHT * 4)
                        
        # animate writing them on screen
        self.play(
            Write(square1),
            Write(circle),
            Write(square2)
        )
        self.wait()
                         
        # fading them from the scene
        self.play(
            FadeOut(square1),
            FadeOut(circle),
            FadeOut(square2),
            run_time=2
        )
