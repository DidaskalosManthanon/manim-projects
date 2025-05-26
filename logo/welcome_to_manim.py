from manim import *

class WelcomToManim(Scene):
    def construct(self):
        words = Text("Welcome to")
        banner = ManimBanner().scale(0.5)
        VGroup(words, banner).arrange(DOWN)

        turn_animation_into_updater(Write(words, run_time=1.5))
        self.add(words)
        self.wait(1.5)
        self.play(banner.expand(), run_time=1.5)
    
