from manim import *


class HelloWorld(Scene):
    def construct(self):
        youtube_red = "#ff0033" # YouTube RED
        self.camera.background_color = youtube_red
        text = Text("Hello world", font_size=144).shift(LEFT)
        self.play(Write(text))
        self.wait()
        yt = Text("YouTube", font_size=144)
        for i in range(len(text) - 5):
            self.play(
                Transform(text[5 + i], yt[i].next_to(text[4 + i], 0.25 * RIGHT))
            )
        self.play(
            Write(yt[5].next_to(text[-1], 0.01 * RIGHT)),
            Write(yt[6].next_to(text[-1], 4 * RIGHT),)
        )
        self.wait()
