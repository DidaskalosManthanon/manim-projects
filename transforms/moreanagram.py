from manim import *


class MoreAnagram(Scene):
    def construct(self):
        src = Text("chien méchant")
        tar = Text("chemin chante")
        self.play(Write(src))
        self.wait()
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait()
        
