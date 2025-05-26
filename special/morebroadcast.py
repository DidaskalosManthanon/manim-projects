from manim import *


class MoreBroadcastExamples(Scene):
    def construct(self):
        BLUE_FR = "#CE1126"
        RED_FR = "#002654"
        circ = Circle(radius=4, color=BLUE_FR)
        square = Square(side_length=4, color=WHITE)
        star = Star(color=RED_FR)
        mobs = [circ, square, star]
        for m in mobs:
            self.play(
                Broadcast(m)
            )
            self.wait(2)
