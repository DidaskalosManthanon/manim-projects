from manim import *


class Anagram(Scene):
    def construct(self):
        src = Text("the morse code")
        tar = Text("here come dots")
        self.play(Write(src))
        self.wait()
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait()
        
