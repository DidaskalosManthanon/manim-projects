from manim import *



class FontsExample(Scene):
    def construct(self):
        
        aelet = Text("Academy Engraved LET", font="Academy Engraved LET")
        self.play(Write(aelet.to_edge(UP)))
        
        at = Text("American Typewriter", font="American Typewriter")
        self.play(Write(at.next_to(aelet, DOWN)))

        ab = Text("Apple Braille", font="Apple Braille")
        self.play(Write(ab.next_to(at, DOWN)))

        ac = Text("Apple Chancery", font="Apple Chancery")
        self.play(Write(ac.next_to(ab, DOWN)))

        ace = Text("Apple Color Emoji", font="Apple Color Emoji")
        self.play(Write(ace.next_to(ac, DOWN)))

        
        

        
